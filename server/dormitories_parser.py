import json
import requests

URL = "http://127.0.0.1:8000"
TABLE_LOCATIONS = "/locations"
TABLE_DORMITORIES = "/dormitories"
TABLE_DETAILS = "/details"
TABLE_ROOMS = "/rooms"
f = open('../jsons/accomodations.json')
data = json.load(f)
blacklist = ["details", "rooms"]
count = 0
for obj in data:
    count += 1
    dormitory_json = {}
    for atr in obj:
        if atr not in blacklist:
            dormitory_json[atr] = obj[atr]
    dormitory_json["detailId"] = count
    db_dormitory = requests.post(f"{URL}{TABLE_DORMITORIES}", json=dormitory_json)
    dormitory = db_dormitory.json()

    location = obj["details"]["locationId"]
    db_location = requests.post(f"{URL}{TABLE_LOCATIONS}", json=location)
    location = db_location.json()

    detail = obj["details"]
    detail["locationId"] = location["id"]
    detail["dormitoryId"] = dormitory["id"]
    # print(json.dumps(detail))
    db_detail = requests.post(f"{URL}{TABLE_DETAILS}", json=detail)
    obj["details"] = detail

    rooms = obj["rooms"]
    for room in rooms:
        room_json = rooms[room]
        room_json["dateFrom"] = room_json["details"]["dateRange"]["from"]
        room_json["dateTo"] = room_json["details"]["dateRange"]["to"]
        del room_json["details"]["dateRange"]
        room_json["dormitoryId"] = dormitory["id"]
        db_room = requests.post(f"{URL}{TABLE_ROOMS}", json=room_json)
