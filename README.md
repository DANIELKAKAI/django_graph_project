# django_graph_project
In this project I have set up a django application that exposes a RESTful Api endpoint using django Channels 
that is used to send and recieve messages between the client and the server.<br/>
Use the following commands to install dependancies and to start the local development server:
```
pip install -r requirements.txt

python manage.py runserver
```
Using a Web socket the client requests for random numbers from the server:<br/>
graph.html line 37
```javascript
var cnt = 0;

    var interval = setInterval(function () {


        chatSocket.send(JSON.stringify({
            'message': "data request"
        }));


        if (cnt === 100) clearInterval(interval);
    }, 300);

```
On recieving the request from the client the server then responds with a random number :
```python
# myapp/consumers.py
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
  ```
  The random number is used by the client to plot a graph using the plotly library:<br/>
  graph.html line 48
  ```javascript
  chatSocket.onmessage = function (e) {
        var data = JSON.parse(e.data);
        var randomNumber = data['data'];

        Plotly.extendTraces('graph', {
            y: [[randomNumber], [randomNumber]]
        }, [0, 1])

    };
  ```
 
