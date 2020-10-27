import requests
import json
from enum import Enum

class State(Enum):
    CHAT_SELECT = 1
    SENDING_MESSAGE = 2

# while (input_str != "quit"):

jfile = open("info.json", 'r')
info = json.load(jfile)
jfile.close()
if info['username'] == "":
    x = requests.get('http://localhost:8000/server/login')
    info['username'] = x.headers['username']

x = requests.get('http://localhost:8000/server/list')
chat_list = json.loads(x.text)

for index, item in enumerate(chat_list):
    print("Select one of the following chatrooms:")
    print(str(index + 1) + ". " + item)

selected_chat = chat_list[int(input()) - 1]

join_headers = {'username': info['username'], 'room': selected_chat}
x = requests.get('http://localhost:8000/server/join', headers=join_headers)
