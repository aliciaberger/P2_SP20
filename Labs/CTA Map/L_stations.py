# Folium train map


# 15pts - Use folium to plot all of the L train stops in Chicago. Use an appropriate start zoom level.
# 5pts - Add the name to each stop as a popup. Add a train icon to each marker.  Save as an html page in the same folder.
# 3pts  - Color code all of the lines (make the pink line marker pink etc.)
# 2pts - Brown is not a default color name.  See if you can use the documentation for Folium to set a marker color through other means.

# Data set is in this folder, but can be found at: https://data.cityofchicago.org/api/views/8pix-ypme/rows.csv?accessType=DOWNLOAD

# Tricky parts of this one
## The location is in tuple format.  If you have trouble converting it, try this:
#my_string = '(41.2, -87.9)'
#my_tuple = eval(my_string)
#print(my_tuple)
#print(type(my_tuple))


import csv
import matplotlib.pyplot as plt
with open("CTA_-_System_Information_-_List_of__L__Stops (1).csv") as f:
    cr = csv.reader(f)
    data = list(cr)
print(len(data))
headers = data.pop(0)
print(headers)

stop_name = [x[2] for x in data]
print(stop_name)

locations_list = []

for x in data:
    locations_list.append([x[-1] for x in data])
print(locations_list[:])
for location in locations_list:
    print(type(location))


#for location in locations_list:
 #   my_string = eval(locations_list)
  #  my_tuple = eval(my_string)
   # print(my_tuple)
    #print(type(my_tuple))

# If you have extra time, try to put some html into the popup.

