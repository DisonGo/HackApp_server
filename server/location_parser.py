import json
import requests
URL = "http://127.0.0.1:8000"
TABLE = "/locations"
f = open('../jsons/accomodations.json')
data = json.load(f)
for obj in data:
    location = obj["details"]["main-info"]
    requests.post(f"{URL}{TABLE}", json=location)
