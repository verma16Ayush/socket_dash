from channels.generic.websocket import AsyncWebsocketConsumer
import json

class Dashboard(AsyncWebsocketConsumer):
    async def connect(self):
        self.groupname = 'dashboard'
        # print(self.scope)
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )
        await self.accept()
    
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.groupname,
            self.channel_name
        )
        # await self.disconnect(code)
    
    async def receive(self, text_data):
        datapoint = json.loads(text_data)
        val = datapoint['value']
        await self.channel_layer.group_send(
            self.groupname,
            {
                'type': 'preprocess',
                'value': val,
            }
        )
        print(text_data)
    
    async def preprocess(self, event):
        val = event['value']
        await self.send(text_data=json.dumps({'value': val}))