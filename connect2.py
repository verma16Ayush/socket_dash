import websocket
import json
from time import sleep
binance_socket = websocket.WebSocket()
my_socket = websocket.WebSocket()
my_socket.connect('ws://localhost:8000/ws/')
request = {
    "method": "SUBSCRIBE",
    "params": [
        "btcusdt@aggTrade",
        "btcusdt@depth"
    ],
    "id": 1
}
binance_socket.connect('wss://stream.binance.com:9443/ws/ethusdt@kline_1m')
print('connection estd')
while(binance_socket.connected):
    sleep(1)
    k = json.loads(binance_socket.recv())
    print(k['k']['n'])
    my_socket.send(json.dumps({'value': k['k']['n']}))
# ws.send(json.dumps())