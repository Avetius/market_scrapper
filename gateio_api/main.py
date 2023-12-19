# main.py
import asyncio
import json

from pubsub import publish_message, wait_for_redis
from futures import list_futures_contracts

async def main():
    while True:
        try:
            await wait_for_redis()
            print("Redis is available gate_api!")
            json_string = list_futures_contracts()
            resultlist =json.loads(json_string)
            names = [item['name'] for item in resultlist if "name" in item]
            print(F"Names LENGTH >>> {len(names)}")
            publish_message(json_string, 'futureContracts')
            await asyncio.sleep(60)
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

