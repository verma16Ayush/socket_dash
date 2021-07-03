import websocket
from time import sleep
import random
import json
# import redis
ws = websocket.WebSocket()
ws.connect('ws://localhost:8000/ws/')
for i in range(100):
    sleep(3)
    val = random.randint(1, 100)
    ws.send(json.dumps({'value': val}))
    print(val)

# wss://stream.binance.com:9443