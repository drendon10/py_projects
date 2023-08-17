# This is a basic web scraper I used to understand how web scraping works

import requests
from bs4 import BeautifulSoup
import csv

page_to_scrape = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

# returns all quotes and authors as a list
quotes = soup.findAll("span", attrs={"class":"text"})
authors = soup.findAll("small", attrs={"class":"author"})

file = open("scrapper_quotes.csv", "w")
writer = csv.writer(file)
writer.writerow(["QUOTES", "AUTHORS"])


for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)
    writer.writerow([quote.text, author.text])
file.close()
