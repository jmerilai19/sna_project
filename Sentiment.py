import csv
import os
import json
import time

start = 0
end = 24 * 7 

dictionary = {"covid19": 0, "covid": 0, "omicron": 0, "coronavirus": 0, "corona": 0}

l = len([name for name in os.listdir('./Summary_Sentiment') if os.path.isfile("./Summary_Sentiment/" + name)])

k = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o']
z = 0

while True:
    i = 0
    dictionary.clear()
    dictionary = {"covid19": 0, "covid": 0, "omicron": 0, "coronavirus": 0, "corona": 0}
    print("New set: ", start, " - ", end, " ")
    for filename in os.listdir("Summary_Hashtag"):
        if i >= start and i <= end:

            # Read Summary_Details
            fS = os.path.join("Summary_Hashtag", filename)
            
            rowsSum = []
            with open(fS, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    rowsSum.append(row)

            rowsSum = rowsSum[::100]

            # Read Summary_Hashtag
            s = filename[0:14] + "Summary_Sentiment.csv"
            fH = os.path.join("Summary_Sentiment", s)

            rowsHas = []
            with open(fH, 'r', encoding='utf-8') as file2:
                reader2 = csv.reader(file2)
                for row2 in reader2:
                    rowsHas.append(row2)

            print(f"Reading {fH} and {fS}")

            # Find hashtag + like combination and store to dictionary
            for rowS in rowsSum:
                zz = rowS[1].lower()
                if zz == "#covid19":
                    for rowH in rowsHas:
                        if rowH[0] == rowS[0]:
                            dictionary["covid19"] += float(rowH[4])
                elif zz == "#covid":
                    for rowH in rowsHas:
                        if rowH[0] == rowS[0]:
                            dictionary["covid"] += float(rowH[4])
                elif zz == "#omicron":
                    for rowH in rowsHas:
                        if rowH[0] == rowS[0]:
                            dictionary["omicron"] += float(rowH[4])
                elif zz == "#coronavirus":
                    for rowH in rowsHas:
                        if rowH[0] == rowS[0]:
                            dictionary["coronavirus"] += float(rowH[4])
                elif zz == "#corona":
                    for rowH in rowsHas:
                        if rowH[0] == rowS[0]:
                            dictionary["corona"] += float(rowH[4])
            

        i += 1
        print(i)
    print(dictionary)
    # Save dictionary as JSON
    hashtag_count = open("./senfilesneg/{}_sen-_{}-{}.json".format(k[z], start, end), "w")
    json.dump(dictionary, hashtag_count)
    hashtag_count.close()

    z += 1

    start = end + 1
    end = min(start + 24*7, 2369)
    if end == 2369:
        break