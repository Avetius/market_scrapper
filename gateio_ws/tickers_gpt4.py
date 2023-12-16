import websocket
import json
import threading
import time 

def on_message(ws, message):
    print("Received:", message)

def on_error(ws, error):
    print("Error:", error)

def on_close(ws, close_status_code, close_msg):
    print("### Closed ###")

def on_open(ws):
    def run(*args):
        # Subscribe to a specific channel, e.g., BTC futures trades
        subscribe_message = {
            "time": int(time.time()),
            "channel": "futures.trades",
            "event": "subscribe",
            "payload": ["BTC_USDT_20231211"]
        }
        ws.send(json.dumps(subscribe_message))
        print("Subscribed to BTC_USDT trades")

    threading.Thread(target=run).start()

if __name__ == "__main__":
    print(f"{int(time.time())}")
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://fx-ws-testnet.gateio.ws/v4/ws/delivery/usdt",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever()