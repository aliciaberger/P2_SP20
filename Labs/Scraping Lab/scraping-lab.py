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
print(days)
print(type(days))

synopsis = soup.find(class_="")
print(days)
print(type(days))


for day in days:
    print(day.text)
    print(synopsis.text)
    print()

#by css class
'''
print("\n" * 10)
quotes = soup.find_all(class_="quote")
print(quotes[0].prettify())

# drill down using dot notation

print(quotes[0].span)
print(quotes[0].span.text)

for quote in quotes:
    print(quote.span.text)

for i in range(len(quotes)):
    print(quotes[i])
    print("\t\t---{}".format(authors[i].text))
    print()

quotes = soup.find_all("span", class_="text", itemprop="text")

for quote in quotes:
    print(quote.text)

'''