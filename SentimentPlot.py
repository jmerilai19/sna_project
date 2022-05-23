import os
import json
from collections import Counter
import matplotlib.pyplot as plt

pos = []
neg = []

x = []

item = "covid19"

i = 1
for filename in os.listdir("senfiles"):
    fS = os.path.join("senfiles", filename)
    print(filename)
    f = open(fS)
    d = json.load(f)

    for key in d:
        if key == item:
            pos.append(d[key])

    x.append(i)
    i += 1

for filename in os.listdir("senfilesneg"):
    fS = os.path.join("senfilesneg", filename)
    print(filename)
    f = open(fS)
    d = json.load(f)

    for key in d:
        if key == item:
            neg.append(-d[key])

print(pos)
print(neg)

fig, ax = plt.subplots()
plt.plot(x, pos, 'g', label='total logist_positive')
plt.plot(x, neg, 'r', label='total logist_negative')
plt.xlim([1,14])
plt.title(f"Sentiment scores for #{item}")
plt.ylabel("Value")
plt.xlabel("Week")
plt.grid(True)
plt.legend()
plt.show()