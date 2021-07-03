import websocket
import json
from time import sleep
binance_socket = websocket.WebSocket()
my_socket = websocket.WebSocket()
binance_socket.connect('wss://stream.binance.com:9443/ws/ethusdt@kline_1m')
my_socket.connect('ws://localhost:8000/ws/')
print('connection estd')
while(binance_socket.connected):
    sleep(3)
    k = json.loads(binance_socket.recv())
    print(k['k']['n'])
    my_socket.send(json.dumps({
        'num_trades': k['k']['n'],
        'open_price': k['k']['o'],
        }))