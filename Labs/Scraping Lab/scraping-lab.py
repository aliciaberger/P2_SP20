# SCRAPING PROBLEMS

# Weather Scraping (15pts)
# Below is a link to a 10-day weather forecast at weather.com
# Pick the weather for a city that has the first letter as your name.
# Use requests and BeautifulSoup to scrape data from the weather table.
# Print a synopsis of the weather for the next 10 days.
# Include the day and date, description, high and low temp, chance of rain, and wind. (2pts each)
# Print the weather for each of the next 10 days to the user in a readable sentences.
# You can customize the text as you like, but it should be readable as a sentence without errors. (5pts)
# You will need to target specific classes or other attributes to pull some parts of the data.
# Sample sentence:
# Wednesday, April 4 will be Partly Cloudy/Windy with a High of 37 degrees and a low of 25, humidity at 52%.  There is 0% chance of rain with winds out of the WNW at 22 mph.
# if the sentence is a little different than shown, that will work; do what you can.  Don't forget about our friend string.format()

from bs4 import BeautifulSoup
import requests

url = "https://weather.com/weather/tenday/l/0df6c5abacc433681eec19026bb8b030e3ccf3b69830725cb987ada967f618cf" #uniform resource locator

page = requests.get(url)
#print(page)  #prints the response

print(page.text)

soup = BeautifulSoup(page.text, "html.parser")
print(soup.prettify()) #nicer way to look at it

#find some data by the tag name
#find method
title = soup.find("title") #title is  just the  tag name
print(title)
print(title.text)


#by attribute

print("\n" * 10)
days = soup.find_all(class_="day-detail clearfix")
days_list = [x.text for x in days]

infos = soup.find_all("td", class_="description")
infos_list = [x.text for x in infos]

temps = soup.find_all("td", class_="temp")
temps_list = [x.text for x in temps]

rains = soup.find_all("td", class_="precip")
rains_list = [x.text for x in rains]

winds = soup.find_all("td", class_="wind")
winds_list = [x.text for x in winds]


hums = soup.find_all("td", class_="humidity")
hums_list = [x.text for x in hums]

print("Welcome to the next 10 days of weather in Aachen, the city that has some of the biggest horse shows in the world.")
print()
for i in range(10):
    print("On", days_list[i], "its looks like it will be", infos_list[i], "with the high and low being", temps_list[i], "and the chance of rain being", rains_list[i], ".", "The winds should be", winds_list[i], "with a humitity of", hums_list[i], ".")

print("Enjoy your time in aachen. Rain or shine the shows will continue so make sure to grab a good seat.")

