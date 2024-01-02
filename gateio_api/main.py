# main.py
import asyncio
import json

from pubsub import publish_message, wait_for_redis
from helper import list_to_string 
from futures import list_futures_contracts
from delivery import list_delivery_contracts
from spot import list_spot_contracts

async def main():
    while True:
        try:
            await wait_for_redis()
            print("Redis is available gate_api!")
            futureslist = list_futures_contracts()
            names = [item['name'] for item in futureslist if "name" in item]
            print(F"future pairs length >>> {len(names)}")
            publish_message("futureContracts", list_to_string(names))
            deliverieslist = list_delivery_contracts()
            deliverynames = [item['name'] for item in deliverieslist if "name" in item]
            print(F"delivery pairs length >>> {len(deliverynames)}")
            publish_message("deliveryContracts", list_to_string(deliverynames))
            spotlist = list_spot_contracts()
            # print(f"spotlist >>> {spotlist}")
            spotnames = [item['currency'] for item in spotlist if "currency" in item]
            print(F"spot pairs length >>> {len(spotnames)}")
            publish_message("spotContracts", list_to_string(spotnames))
            # 
            await asyncio.sleep(10)
        except TimeoutError as e:
            print(f"Error: {e}")
            # Handle the timeout error

        await asyncio.sleep(1)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()

