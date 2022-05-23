import os
import json
from collections import Counter
import matplotlib.pyplot as plt


covid19 = 0
covid = 0
noolvidamos = 0
omicron = 0
longcovid = 0

for filename in os.listdir("RT20x"):
    fS = os.path.join("RT20x", filename)
    print(filename)
    f = open(fS)
    d = json.load(f)

    if "covid19" in d:
        covid19 += d["covid19"]

    if "covid" in d:
        covid += d["covid"]

    if "noolvidamos" in d:
        noolvidamos += d["noolvidamos"]

    if "omicron" in d:
        omicron += d["omicron"]

    if "longcovid" in d:
        longcovid += d["longcovid"]

covid19 = covid19/14
covid = covid/14
noolvidamos = noolvidamos/14
omicron = omicron/14
longcovid = longcovid/14

print(covid19)
print(covid)
print(noolvidamos)
print(omicron)
print(longcovid)