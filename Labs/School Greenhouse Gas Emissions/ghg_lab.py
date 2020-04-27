
'''
Greenhouse gas emissions (GHG) vs. square footage for all school buildings in Chicago

Data set used will be Chicago Energy Benchmark info from 2018
data can be found at...
https://data.cityofchicago.org/api/views/xq83-jr8c/rows.csv?accessType=DOWNLOAD

Energy Efficiency of Chicago Schools (35pts)

Chicago requires that all buildings over 50000 square feet in the city comply with energy benchmark reporting each year.
The data set at the link above is that data from 2015 to 2018.
We will use this data to look at schools.  We will visualize the efficiency of schools by scatter plot.
We expect that the more square footage (sqft) a school is, the more greenhouse gas (ghg) emission it will produce.
Challenge (for fun):
An efficient school would have a large ratio of sqft to ghg.
It would also be interesting to know where Parker lies on this graph???  Let's find out.

Make a scatterplot which does the following:
- Scatter plot the Total Greenhouse gas (GHG) Emmissions (y-axis), versus building square footage (x-axis) (10pts)
- Data includes ONLY data for K-12 Schools. (5pts)
- Data includes ONLY data for 2018 reporting. (5pts)
- Label x and y axis and give appropriate title. (5pts)
- Annotate Francis W. Parker. (5pts)
- Create a best fit line for schools shown. (5pts)


Extra Credit: Add a significant feature to your graph that helps tell the story of your data.  (feel free to use methods from matplotlib.org). (10pts)

Note: With extra credit you will earn you a max of 35pts (100%) for the assignment.
Maybe you can try one of the following or think up your own:
- Annotated labels (school name) for the 3 highest and 3 lowest GHG Intensities.
- Make schools in top 10 percent of GHG Intensity show in green.
- Make schools in bottom 10 percent GHG Intesity show in red.
- Add colleges and universities (use a different marker type)


Note 2:  This is a tough assignment to do on your own.  Do your best with what you have.
'''

import csv
import requests
import matplotlib.pyplot as plt
import numpy as np

def get_data(url):
    with requests.Session() as s:
        download = s.get(url)
        content = download.content.decode('utf-8')
        reader = csv.reader(content.splitlines(), delimiter=',')
        my_list = list(reader)
    return my_list


data = get_data("https://data.cityofchicago.org/api/views/xq83-jr8c/rows.csv?accessType=DOWNLOAD")
header = data.pop(0)

print(header)

ghg_index = header.index("Total GHG Emissions (Metric Tons CO2e)")
sqft_index = header.index("Gross Floor Area - Buildings (sq ft)")
type_index = header.index("Primary Property Type")


valid_data = []
print(len(data))

for building in data:
    try:
        int(building[ghg_index])
        int(building[sqft_index])
        if building[type_index] == "K-12 School":
            valid_data.append(building)
    except:
        pass

print(len(valid_data))

ghg = [int(x[ghg_index]) for x in valid_data]
color = []
for building in ghg:
    if building > 4000:
        color.append("red")
    elif building < 350:
        color.append("green")
    else:
        color.append("yellow")


sqft = [int(x[sqft_index]) for x in valid_data]

p = np.polyfit(sqft, ghg, 1)  # (x, y, poly_order)  1st order is linear
print(p)
x = [x for x in range(750000)]
y = [p[0] * y + p[1] for y in x]
plt.plot(x, y)


plt.figure(1, tight_layout=True)


plt.scatter(sqft, ghg, c=color, marker='*')  # s for size, c for color (arrays
plt.ylabel("Square footage")
plt.xlabel("Total Greenhouse Gas Emisions")
plt.title("Square footage vs gas emisions")
#plt.annotate("Francis Parker", xy=(sqft[543], ghg[543]))     something is wrong here
plt.legend()

plt.show()
