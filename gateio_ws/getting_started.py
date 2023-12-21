import os
import asyncio
from dotenv import load_dotenv

from gate_ws import Configuration, Connection, WebSocketResponse
from gate_ws.spot import SpotPublicTradeChannel

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

# define your callback function on message received
def print_message(conn: Connection, response: WebSocketResponse):
    if response.error:
        print('error returned: ', response.error)
        conn.close()
        return
    print(response.result)


async def main():
    # initialize default connection, which connects to spot WebSocket V4
    # it is recommended to use one conn to initialize multiple channels
    conn = Connection(Configuration())

    # subscribe to any channel you are interested into, with the callback function
    channel = SpotPublicTradeChannel(conn, print_message)
    channel.subscribe(["GT_USDT"])

    # start the client
    await conn.run()


if __name__ == '__main__':
   loop = asyncio.get_event_loop()
   loop.run_until_complete(main())
   loop.close()