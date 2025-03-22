import json
from collections import Counter

with open("data/generated.json", "r", encoding="utf-8") as f:
    data = json.load(f)

all_tags = []
for item in data["issues"]:
    all_tags.extend(item.get("tags", []))

counter = Counter(all_tags)

for tag, count in counter.most_common():
    print(f"{tag}: {count}")
