import json
import requests

URL = "http://127.0.0.1:8000"
TABLE_UNIVERSITIES = "/universities"

f = open('../jsons/universities.json')
data = json.load(f)
blacklist = ["details", "rooms"]
count = 0
for obj in data:
    db_university = requests.post(f"{URL}{TABLE_UNIVERSITIES}", json=obj)