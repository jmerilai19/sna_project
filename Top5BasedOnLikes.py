import os
import json
from collections import Counter


dictionary1 = {}

for filename in os.listdir("Likes70"):
    fS = os.path.join("Likes70", filename)

    f = open(fS)
    d = json.load(f)

    for key in d:
        if key in dictionary1:
            dictionary1[key] = dictionary1[key] + int(d[key])
        else:
            dictionary1[key] = int(d[key])

hashtag_count = open("total_likes70.json", "w")
json.dump(dictionary1, hashtag_count)
hashtag_count.close()

dictionary2 = {}

f = open('total_likes70.json')
d = json.load(f)

k = Counter(d)

high = k.most_common(6)

for i in high:
    print(i[0],": ",i[1]," ")