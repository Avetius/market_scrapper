# !/usr/bin/env python
# coding: utf-8
# import os
# import time
# import logging
# import schedule
import asyncio
from pubsub import subscribe_channel, wait_for_redis
from helpers import string_to_list
# from dotenv import load_dotenv
from gate_ws import Configuration, Connection, WebSocketResponse
from gate_ws.spot import SpotPublicTradeChannel
from gate_ws.futures import FuturesPublicTradeChannel


# load_dotenv()
# Access environmental variables
# API_KEY = os.getenv("API_KEY")
# API_SECRET = os.getenv("API_SECRET")

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

async def my_callback(conn, response):
    print(response.result)
    await asyncio.sleep(1)

# print(API_KEY)

# logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.DEBUG)

async def main():
    try:
        await wait_for_redis()
        print("Redis is available sub2!")
        resultstr = subscribe_channel('futureContracts')
        trading_pairs = string_to_list(resultstr)
        # provide default callback for all channels
        spot_conn = Connection(Configuration(app='spot')) # lambda c, r: print(r.result)
        futures_conn = Connection(Configuration(app='futures', settle='usdt', test_net=False))
        # default callback will be used if callback not provided when initializing channels
        spotchannel = SpotPublicTradeChannel(spot_conn, my_callback)
        spotchannel.subscribe(trading_pairs) # ["GT_USDT"] 

        futurechannel = FuturesPublicTradeChannel(futures_conn, my_callback) # lambda c, r: print(r.result)
        futurechannel.subscribe(trading_pairs) # ["BTC_USDT"]
        futurechannel.unsubscribe(["BTC_USDT", "ETH_USDT"])

        # start both connection
        await asyncio.gather(
            spot_conn.run(),
            futures_conn.run()
        )
    except TimeoutError as e:
        print(f"Error: {e}")
        # Handle the timeout error

    await asyncio.sleep(1)


if __name__ == '__main__':
    print("STARTING WEBSOCKET")
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()

