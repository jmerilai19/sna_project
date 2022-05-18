import json
from collections import Counter


f = open("entity_count.json")
dictionary = json.load(f)

k = Counter(dictionary)

high = k.most_common(5)

for i in high:
    print(i[0],": ", i[1], " ")