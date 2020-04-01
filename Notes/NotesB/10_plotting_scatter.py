import csv
import matplotlib.pyplot as plt
import numpy as np

with open("World firearms murders and ownership - Sheet 1.tsv") as f:
    reader = csv.reader(f, delimiter='\t')
    data = list(reader)

header = data.pop(0)
print(header)

# make a scatter of firearms_per_100 vs homicides_100k

homicide_100k = []
firearms_100 = []
countries = []

for country in data:
    try:
        homicides = float(country[5])
        firearms = float(country[-2])
        name = country[0]
        homicide_100k.append(homicides)
        firearms_100.append(firearms)
        countries.append(name)
    except:
        print(country[0], "data is inadequate.")

print(countries)








plt.figure("Homisides per Firearm")
plt.scatter(firearms_100, homicide_100k)
plt.ylabel("homisides per 100k")
plt.xlabel("firearms per 100k")


#best fit line
p = np.polyfit(firearms_100, homicide_100k, 1) #(x, y, order) linearis first order
print(p)
x = [x for x in range(100)]
y = [p[0] * y + p[1] for y in x]


plt.plot(x,y)

plt.show()