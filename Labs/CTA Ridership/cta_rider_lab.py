'''
CTA Ridership (25pts)

Get the csv from the following data set.
https://data.cityofchicago.org/api/views/w8km-9pzd/rows.csv?accessType=DOWNLOAD
This shows CTA ridership by year going back to the 80s
It has been updated with 2018 data, but not yet with 2019 unfortunately
'''

import csv
import matplotlib.pyplot as plt

with open("CTA_-_Ridership_-_Annual_Boarding_Totals (1).csv") as f:
    cr = csv.reader(f)
    data = list(cr)
print(len(data))
headers = data.pop(0)
print(headers)

#1  Make a line plot of rail usage for the last 10 years of data.  (year on x axis, and ridership on y) (5pts)
data.sort(key=lambda x: int(x[0]))  # sorts by whatever is in there
print(data)

years = [x[0] for x in data]
top_ten = years[-10:]
print(top_ten)

rail = [int(x[-2]) for x in data]
rail_ten = rail[-10:]
print(rail_ten)


#2  Plot bus usage for the same years as a second line on your graph. (5pts)

bus = [int(x[1]) for x in data]
bus_ten = bus[-10:]
print(bus_ten)



#3  Plot total usage on a third line on your graph. (5pts)
total = [int(x[-1]) for x in data]
total_ten = total[-10:]
print(total_ten)



plt.title("Last ten years transit")
plt.ylabel('Number of Rides')
plt.xlabel('Years')
plt.plot(top_ten, total_ten, color='red', label='total')
plt.plot(top_ten, rail_ten, color='darkgreen', label='rail')
plt.plot(top_ten, bus_ten, color='blue', label='bus')
plt.legend()
plt.show()
#4  Add a title and label your axes. (4pts)



#5  Add a legend to show data represented by each of the three lines. (4pts)


#6  What trend or trends do you see in the data?  Offer a hypotheses which might explain the trend(s). Just add a comment here to explain. (2pts)

'''
When looking at the data is seems that as of recently the number of rides that public transportation have is decreasing
I belive this is due to a combination of more people walking/riding bikes, mroe people taking their own viechals and 
and with the new technology more people can work from home so less people new to take public transit

'''

