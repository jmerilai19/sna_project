import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import t
import numpy as np
import math
import time
import os
import csv
import json

# calculate runtime
start_time = time.time()

tinv = lambda p, df: abs(t.ppf(p/2, df))

dictionary = {}

for filename in os.listdir("Summary_Hashtag"):
    f = os.path.join("Summary_Hashtag", filename)

    print(filename)

    rows = []

    with open(f, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    for row in rows:
        if row[0] != 'Tweet_ID':
            z = row[1].lower()
            if z in dictionary:
                dictionary[z] = dictionary[z] + 1
            else:
                dictionary[z] = 1

hashtag_count = open("hashtag_count.json", "w")
json.dump(dictionary, hashtag_count)
hashtag_count.close()

# collect values to array
freq = []
for key in dictionary:
    freq.append(dictionary[key])

y = []
x = []

# new array for log values
for key in dictionary:
    y.append(math.log(dictionary[key]))

# index values for x axis
for i in range(1, len(y) + 1):
    x.append(math.log(i))

# sort for graph
y = sorted(y, reverse=True)

# convert for np
y = np.array(y)
x = np.array(x)

# power law
res = stats.linregress(x, y)

ts = tinv(0.05, len(x)-2)
#print(f"slope (95%): {res.slope:.6f} +/- {ts*res.stderr:.6f}")
#print(f"intercept (95%): {res.intercept:.6f}" f" +/- {ts*res.intercept_stderr:.6f}")


# runtime
print(time.time() - start_time)

# plot
fig, ax = plt.subplots()
plt.scatter(x, y, s=0.5, c="b", label='distribution')
plt.plot(x, res.intercept + res.slope*x, 'r', label='power-law')
plt.title("Number of tweets per hashtag")
plt.ylabel("log(Number of tweets)")
plt.xlabel("Hashtag index")
plt.grid(True)
ax.tick_params(labelbottom=False)
plt.legend()
plt.show()
