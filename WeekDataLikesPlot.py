import os
import json
from collections import Counter
import matplotlib.pyplot as plt


covid19 = []
covid = []
omicron = []
corona = []
saludmental = []

weeks = []

i = 1

for filename in os.listdir("LikeWeek70"):
    fS = os.path.join("LikeWeek70", filename)
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

    if "corona" in d:
        corona.append(d["corona"])
    else:
        corona.append(0)

    if "saludmental" in d:
        saludmental.append(d["saludmental"])
    else:
        saludmental.append(0)

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
plt.plot(weeks, corona, 'y', label='#corona')
plt.plot(weeks, saludmental, 'm', label='#saludmental')
plt.title("Evolution of the Top 5 Hashtags (Likes)")
plt.ylabel("Value")
plt.xlabel("Week")
plt.grid(True)
plt.legend()
plt.show()