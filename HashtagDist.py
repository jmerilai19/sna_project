import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import t
from scipy.optimize import curve_fit
import numpy as np
import math
import time
import json

# calculate runtime
start_time = time.time()

tinv = lambda p, df: abs(t.ppf(p/2, df))

file = open("hashtag_count.json")
dictionary = json.load(file)

newD = {}

for key in dictionary:
    a = str(dictionary[key])
    if a in newD:
        newD[a] += 1
    else:
        newD[a] = 1

hashtag_dist = open("hastag_dist_sampled.json", "w")
json.dump(newD, hashtag_dist)
hashtag_dist.close()

print("Done")

x = []
y = []
# new array for log values
for key in newD:
    y.append(math.log(newD[key]))
    x.append(math.log(int(key)))


# convert for np
y = np.array(y)
x = np.array(x)

print("Next is linregress")

res = stats.linregress(x=x, y=y)

ts = tinv(0.05, len(x)-2)
print(f"slope (95%): {res.slope:.6f} +/- {ts*res.stderr:.6f}")
print(f"intercept (95%): {res.intercept:.6f}" f" +/- {ts*res.intercept_stderr:.6f}")

# runtime
print(time.time() - start_time)

# plot
plt.scatter(x , y, s=0.6, c="b", label='distribution')
plt.plot(x, res.intercept + res.slope*x, 'r', label='power-law')
plt.ylim([-0.1, 15])
plt.xlim([0, 14])
plt.title("Distribution of the hashtags in terms of number of tweets citing the hashtag")
plt.ylabel("Number of hashtags (log)")
plt.xlabel("Number of tweets (log)")
plt.grid()
plt.legend()
plt.show()