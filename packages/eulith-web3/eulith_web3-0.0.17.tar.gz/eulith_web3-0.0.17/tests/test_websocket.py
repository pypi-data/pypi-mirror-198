import json
import time
from functools import partial
from threading import Event

from eulith_web3.erc20 import TokenSymbol
from eulith_web3.eulith_web3 import EulithWeb3
from eulith_web3.signing import LocalSigner, construct_signing_middleware
from eulith_web3.uniswap import EulithUniswapPoolLookupRequest, UniswapPoolFee, EulithUniswapV3Pool


def test_uni_subscription():
    def message_handler(ws, message, ew3: EulithWeb3, trigger_if_failed: Event):
        result_dict = json.loads(message)

        res = result_dict.get('result')
        if type(res) == str:
            if '0x' not in res:
                print('Failed on result')
                trigger_if_failed.set()

        if type(res) == dict:
            p = res.get('data').get('price')
            if p < 0.000810 or p > 0.000820:
                print('Failed on price')
                trigger_if_failed.set()

    def error_handler(ws, error, ew3, trigger_if_received: Event):
        trigger_if_received.set()

    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    ew3 = EulithWeb3(eulith_url="http://localhost:7777/v0",
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ."
                                          "eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0."
                                          "G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     signing_middle_ware=construct_signing_middleware(acct))

    proxy_address = ew3.v0.ensure_toolkit_contract(acct.address)

    weth = ew3.v0.get_erc_token(TokenSymbol.WETH)
    usdc = ew3.v0.get_erc_token(TokenSymbol.USDC)

    sell_amount = 2

    # approve the transfer from the wallet to cover the sell side of the swap
    tx = weth.approve(proxy_address, int(sell_amount * 1.2 * 10 ** weth.decimals),
                      {'gas': 100000, 'from': acct.address})
    ew3.eth.send_transaction(tx)

    uni_pool = ew3.v0.get_univ3_pool(params=EulithUniswapPoolLookupRequest(
        token_a=weth,
        token_b=usdc,
        fee=UniswapPoolFee.FiveBips
    ))

    test_failed_in_thread = Event()
    received_error = Event()

    # make sure a valid pool is correctly handled
    uni_pool.subscribe_prices(
        message_handler=partial(message_handler, trigger_if_failed=test_failed_in_thread),
        error_handler=partial(error_handler, trigger_if_received=received_error)
    )

    # make sure that basic error handling works
    bad_uni_pool = EulithUniswapV3Pool(ew3, ew3.to_checksum_address('0x24C09eA523e9260E2187D5BAF4F767b48653F63C'))
    bad_uni_pool.subscribe_prices(
        message_handler=partial(message_handler, trigger_if_failed=test_failed_in_thread),
        error_handler=partial(error_handler, trigger_if_received=received_error))

    price, fee, r = uni_pool.get_quote(weth, sell_amount, pay_transfer_from=acct.address)

    ew3.v0.start_atomic_transaction(acct.address)
    ew3.v0.start_uni_swap(r)
    ew3.v0.finish_inner()
    tx = ew3.v0.commit_atomic_transaction()

    tx['gas'] = 1000000
    tx_hash = ew3.eth.send_transaction(tx)

    r = ew3.eth.wait_for_transaction_receipt(tx_hash)
    assert r.status == 1

    ew3.websocket_conn.disconnect()

    assert not test_failed_in_thread.is_set()
    assert received_error.is_set()


def test_basic_sub_unsub():
    def message_handler(ws, message, ew3):
        pass

    def error_handler(ws, error, ew3):
        pass

    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    ew3 = EulithWeb3(eulith_url="http://localhost:7777/v0",
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ."
                                          "eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0."
                                          "G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     signing_middle_ware=construct_signing_middleware(acct))

    weth = ew3.v0.get_erc_token(TokenSymbol.WETH)
    usdc = ew3.v0.get_erc_token(TokenSymbol.USDC)

    uni_pool = ew3.v0.get_univ3_pool(params=EulithUniswapPoolLookupRequest(
        token_a=weth,
        token_b=usdc,
        fee=UniswapPoolFee.FiveBips
    ))

    # make sure a valid pool is correctly handled
    subscription_handle = uni_pool.subscribe_prices(
        message_handler=message_handler,
        error_handler=error_handler)

    # let the server respond with a subscription id
    time.sleep(0.5)

    assert len(ew3.websocket_conn.subscriptions) == 1

    subscription_handle.unsubscribe()

    # let the server process the unsub request
    time.sleep(0.5)

    assert len(ew3.websocket_conn.subscriptions) == 0

    ew3.websocket_conn.disconnect()


def test_connection_goes_down():
    def message_handler(ws, message, ew3):
        pass

    def error_handler(ws, error, ew3):
        pass

    acct = LocalSigner("0x4d5db4107d237df6a3d58ee5f70ae63d73d7658d4026f2eefd2f204c81682cb7")
    ew3 = EulithWeb3(eulith_url="http://localhost:7777/v0",
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ."
                                          "eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0."
                                          "G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw",
                     signing_middle_ware=construct_signing_middleware(acct))

    weth = ew3.v0.get_erc_token(TokenSymbol.WETH)
    usdc = ew3.v0.get_erc_token(TokenSymbol.USDC)

    uni_pool = ew3.v0.get_univ3_pool(params=EulithUniswapPoolLookupRequest(
        token_a=weth,
        token_b=usdc,
        fee=UniswapPoolFee.FiveBips
    ))

    # make sure a valid pool is correctly handled
    uni_pool.subscribe_prices(
        message_handler=message_handler,
        error_handler=error_handler)

    # let the server respond with a subscription id
    time.sleep(0.5)

    assert len(ew3.websocket_conn.subscriptions) == 1
    old_sub_id = list(ew3.websocket_conn.subscriptions.keys())[0]

    ew3.websocket_conn.disconnect()

    assert len(ew3.websocket_conn.subscriptions) == 1

    ew3.websocket_conn.connect()

    # give some time for subscription to come back
    time.sleep(0.5)

    # subscription is back
    assert len(ew3.websocket_conn.subscriptions) == 1
    new_sub_id = list(ew3.websocket_conn.subscriptions.keys())[0]
    assert old_sub_id != new_sub_id

    ew3.websocket_conn.disconnect()
