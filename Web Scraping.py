import requests
from bs4 import BeautifulSoup as soup
import random
'''
for i in range(1, 11):
    url = 'http://quotes.toscrape.com/page/' + str(i)
    page_request = requests.get(url)
    page_html = page_request.text
    page_soup = soup(page_html, 'html.parser')

    # findAll - search by tag name, attribute (kwarg), class (kwarg), string=""
    quotes = page_soup.findAll("span", class_="text") # since class is a keyword in python, this had to be changed to class_
    authors = page_soup.findAll("small", class_="author")

    print("Random quote:", quotes[random.randrange(len(quotes))].text, "\n—", authors[random.randrange(len(authors))].text, end="\n\n")

    for i in range(len(quotes)):
        print(quotes[i].text)
        print("—", authors[i].text, end="\n\n")
'''

# computer science finance
# Spotify started publicly trading
# python stock trading

url = "https://www.regmovies.com/theaters/regal-webster-place-11/C00129681357"
page = requests.get(url)

html = page.text
page_soup = soup(html, 'html.parser')

titles = [x.text.strip() for x in page_soup.findAll("h3", class_="title")]
showtimes = [x.findAll("li") for x in page_soup.findAll("ul", class_="format-showtimes")]

#snow crash

for i in range(11):
    print(titles[i])
    for j in range(len(showtimes[i])):
        print(showtimes[i][j].text.strip())

# "student research project"