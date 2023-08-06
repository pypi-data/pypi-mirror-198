import time

from eulith_web3.erc20 import TokenSymbol
from eulith_web3.eulith_web3 import EulithWeb3
from eulith_web3.uniswap import EulithUniswapPoolLookupRequest, UniswapPoolFee
from eulith_web3.websocket import EulithWebsocketConnection, SubscribeRequest

if __name__ == '__main__':
    ew3 = EulithWeb3(eulith_url="http://localhost:7777/v0",
                     eulith_refresh_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NksifQ.eyJzdWIiOiJsaWJ0ZXN0IiwiZXhwIjoxODQ0Njc0NDA3MzcwOTU1MTYxNSwic291cmNlX2hhc2giOiIqIiwic2NvcGUiOiJBUElSZWZyZXNoIn0.G87Tv9LwLH8SRgjlVKIAPk1pdavVS0xwz3fuB7lxP0Et-pPM7ojQkjC1zlC7zWYUdh9p3GvwX_ROfgSPJsw-Qhw")

    weth = ew3.v0.get_erc_token(TokenSymbol.WETH)
    usdc = ew3.v0.get_erc_token(TokenSymbol.USDC)
    pool = ew3.v0.get_univ3_pool(EulithUniswapPoolLookupRequest(
        token_a=weth,
        token_b=usdc,
        fee=UniswapPoolFee.FiveBips
    ))

    wsc = EulithWebsocketConnection(ew3)

    subscribe_request = SubscribeRequest(
        subscription_type='uni_prices',
        args={
            'pool_address': pool.address
        }
    )

    def handle_something(ws, message, ew3):
        print(message)
        print("got a message!")

    def handle_error(ws, message, ew3):
        print(message)
        print("got an error!")

    sub_handle = wsc.subscribe(subscribe_request, handle_something, handle_error)
