import os
import json
from collections import Counter
import matplotlib.pyplot as plt


covid19 = []
covid = []
omicron = []
mewsuppasit = []
noolvidamos = []

weeks = []

i = 1

for filename in os.listdir("LikeRT"):
    fS = os.path.join("LikeRT", filename)
    print(filename)
    f = open(fS)
    d = json.load(f)

    if "covid19" in d:
        covid19.append(d["covid19"])
    else:
        covid19.append(0)

    if "covid" in d:
        covid.append(d["covid"])
    else:
        covid.append(0)

    if "omicron" in d:
        omicron.append(d["omicron"])
    else:
        omicron.append(0)

    if "mewsuppasit" in d:
        mewsuppasit.append(d["mewsuppasit"])
    else:
        mewsuppasit.append(0)

    if "noolvidamos" in d:
        noolvidamos.append(d["noolvidamos"])
    else:
        noolvidamos.append(0)

    weeks.append(i)

    i += 1

print(covid19)

fig, ax = plt.subplots()
plt.xlim([1, 13])
"""
plt.ylim([0, 1000000])"""
plt.plot(weeks, covid19, 'r', label='#covid19')
plt.plot(weeks, covid, 'b', label='#covid')
plt.plot(weeks, omicron, 'g', label='#omicron')
plt.plot(weeks, mewsuppasit, 'y', label='#mewsuppasit')
plt.plot(weeks, noolvidamos, 'm', label='#noolvidamos')
plt.title("Evolution of the Top 5 Hashtags (Retweets)")
plt.ylabel("Value")
plt.xlabel("Week")
plt.grid(True)
plt.legend()
plt.show()