import csv
import os
import json
import time

start = 0
end = 24 * 7 

dictionary = {"covid19": 0, "noolvidamos": 0, "covid": 0, "mewsuppasit": 0, "omicron": 0}

l = len([name for name in os.listdir('./RT100') if os.path.isfile("./RT100/" + name)])

k = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o']
z = 0

while True:
    i = 0
    dictionary.clear()
    dictionary = {"covid19": 0, "noolvidamos": 0, "covid": 0, "mewsuppasit": 0, "omicron": 0}
    print("New set: ", start, " - ", end, " ")
    for filename in os.listdir("RT100"):
        fS = os.path.join("RT100", filename)
        if i >= start and i <= end:
            start_time = time.time()

            f = open(fS)
            d = json.load(f)

            for key in d:
                if key == "#covid19":
                    dictionary["covid19"] = dictionary["covid19"] + d[key]
                if key == "#covid":
                    dictionary["covid"] = dictionary["covid"] + d[key]
                if key == "#omicron":
                    dictionary["omicron"] = dictionary["omicron"] + d[key]
                if key == "#mewsuppasit":
                    dictionary["mewsuppasit"] = dictionary["mewsuppasit"] + d[key]
                if key == "#noolvidamos":
                    dictionary["noolvidamos"] = dictionary["noolvidamos"] + d[key]
                
            print(filename)
        i += 1
    print(dictionary)
    # Save dictionary as JSON
    hashtag_count = open("./LikeRT/{}_hashtag_rt_{}-{}.json".format(k[z], start, end), "w")
    json.dump(dictionary, hashtag_count)
    hashtag_count.close()

    z += 1

    start = end + 1
    end = min(start + 24*7, 2369)
    if end == 2369:
        break