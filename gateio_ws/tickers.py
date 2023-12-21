from websocket import create_connection

ws = create_connection("wss://fx-ws-testnet.gateio.ws/v4/ws/delivery/usdt")
ws.send(
    '{"time" : 1702206658, "channel" : "futures.tickers", "event": "subscribe", "payload" : ["BTC_USDT_20231212"]}')
print(ws.recv())
