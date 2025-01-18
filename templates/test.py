import json
import flask
import pandas

df = pandas.read_csv("C:/Users/asukh/Documents/Weather_API/data"
                     "/TG_STAID000010.txt"
                     "",skiprows=20,parse_dates=['    DATE'])

result = df[df['    DATE'].dt.year == 2001]
print(result.to_dict(orient="records"))

