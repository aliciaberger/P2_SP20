import matplotlib.pyplot as plt
import csv

with open("Libraries_-_2019_Visitors_by_Location.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

print(len(data))

headers = data.pop(0)
print(headers)

data.sort(key=lambda x: int(x[-1]))
print(data)

library_names = [x[0] for x in data]
print(library_names)

monthly_data = [x[4:-1]for x in data]
print(monthly_data)

my_library = monthly_data[library_names.index('Lincoln Park')]
my_library = [int(x) for x in my_library]
print(my_library)

plt.figure(1, tight_layout=True)
month_numbers = [x for x in range(12)]
month_names = headers[4:-1]
print(month_names)

plt.bar(month_numbers, my_library, color='lightblue', edgecolor='black')
plt.xticks(month_numbers, month_names, rotation=45)  # replaces the shown values on the graph axis
# axis

plt.axis([0, 11, 0, 16000])
plt.title("Lincon park Library")
plt.ylabel('Visitors')





plt.figure(2, tight_layout =True, figsize=(8,8))
#plot every library in chi YTD Visitors

ytd_list = [int(x[-1]) for x in data]
print(ytd_list)
library_numbers = [x for x in range(len(library_names))]

plt.barh(library_numbers, ytd_list)
plt.yticks(library_numbers, library_names, fontsize=6)

plt.show()


