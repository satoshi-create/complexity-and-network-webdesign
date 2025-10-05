import json

with open("response.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    print(data["body"])
