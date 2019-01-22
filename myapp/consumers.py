from channels.generic.websocket import WebsocketConsumer
import json
import random

class GraphConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        random_value = random.randint(1,11)*0.1
        self.send(text_data=json.dumps({
            'data': random_value
        }))