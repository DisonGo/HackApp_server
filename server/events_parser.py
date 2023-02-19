import json
import requests

URL = "http://127.0.0.1:8000"
TABLE_EVENTS = "/events"

f = open('../jsons/events.json')
data = json.load(f)
for obj in data:
    db_event = requests.post(f"{URL}{TABLE_EVENTS}", json=obj)