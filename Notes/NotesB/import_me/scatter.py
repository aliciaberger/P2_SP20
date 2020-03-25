import csv
import matplotlib.pyplot as plt
import numpy as np

with open("Notes/NotesB/World firearms murders and ownership - Sheet 1.tsv") as f:
    reader = csv.reader(f, delimiter='\t')
    data =  list(reader)



header = data.pop(0)
print(header)

homiside_100k = []
firearms_100k= []

for country in data:
    try:
        homiside = float(country[5])
        firearms = float(country[-2])
        name =  country[0]
        homiside_100k.append(homiside)
        firearms_100k.append(firearms)
    except:
        print(country[0], "is inadaquit")