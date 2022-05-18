import csv
import os
import json
import time


d = {} # Dictionary for likes

for filename in os.listdir("Summary_Details"):
    d.clear()
    start_time = time.time()

    # Read Summary_Details
    fS = os.path.join("Summary_Details", filename)
    
    rowsSum = []
    with open(fS, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            rowsSum.append(row)

    rowsSum = rowsSum[::100]

    # Read Summary_Hashtag
    s = filename[0:14] + "Summary_Hashtag.csv"
    fH = os.path.join("Summary_Hashtag", s)

    rowsHas = []
    with open(fH, 'r', encoding='utf-8') as file2:
        reader2 = csv.reader(file2)
        for row2 in reader2:
            rowsHas.append(row2)

    # Find hashtag + like combination and store to dictionary
    for rowS in rowsSum:
        if rowS[3] == 'NO' and int(rowS[5]) > 0:
            for rowH in rowsHas:
                if rowH[0] == rowS[0]:
                    z = rowH[1].lower()
                    if z in d:
                        d[z] = d[z] + int(rowS[5])
                    else:
                        d[z] = int(rowS[5])
                    break

    # Save dictionary as JSON
    hashtag_count = open("./RT100/hashtag_rt_{}.json".format(filename), "w")
    json.dump(d, hashtag_count)
    hashtag_count.close()

    print("{}: {}s.".format(filename, time.time() - start_time))  