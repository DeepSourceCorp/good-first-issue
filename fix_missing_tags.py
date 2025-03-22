import json

with open("data/generated.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data["issues"]:
    if "tags" not in item:
        item["tags"] = []

with open("data/generated.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
