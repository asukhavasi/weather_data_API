import json

import pandas

file = pandas.read_csv("C:/Users/asukh/Documents/Weather_API/static/words"
                       ".csv",sep="|")

print(file["word"])
print(file["definition"])


dict = {}

for i in range(len(file["word"])):
    for index, row in file.iterrows():
        dict["key"] = row["word"]
        dict["value"] = row["definition"]

print(dict)