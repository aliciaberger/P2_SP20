from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/" #uniform resource locator

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
authors = soup.find_all(itemprop="author")
print(authors)
print(type(authors))


for author in authors:
    print(author.text)

#by css class

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