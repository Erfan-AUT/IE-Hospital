import requests
import json

input_str = "start"

# while (input_str != "quit"):
    
x = requests.get('http://localhost:8000/server/login')
username = x.headers['username']
x = requests.get('http://localhost:8000/server/list')
chat_list = json.loads(x.text)
