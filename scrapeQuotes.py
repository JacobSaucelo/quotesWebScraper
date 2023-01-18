import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com/page/1/"
file = open("scrapesQuotes.csv", "w",encoding='utf-8')
writer = csv.writer(file)
writer.writerow(["quotes", "authors"])

def getData(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

def getNextPage(soup):
    page = soup.find("ul",{"class":"pager"})
    if page.find("li",{"class":"next"}):
        url = page.find("li",{"class":"next"}).find("a")["href"]
        return "https://quotes.toscrape.com" + str(url)
    else:
        return

def getQuotes(soup):
    quotes = soup.find_all("span", {"itemprop" : "text"})
    authors = soup.find_all("small", {"itemprop" : "author"})
    for quote ,author in zip(quotes, authors):
        print(quote.text + " -" + author.text)
        writer.writerow([quote.text,author.text])

while True:
    soup = getData(url)
    getQuotes(soup)
    url = getNextPage(soup)
    if not url:
        break
    print(url)
file.close()


# quotes = soup.find_all("span", attrs={"itemprop" : "text"})
# authors = soup.find_all("small", attrs={"itemprop" : "author"})
# nextpage = soup.find("ul", {"class" : "pager"}).find("li",{"class": "next"})

# print(getNextPage(getData(url)))

# if nextpage:
#     print(nextpage.find("a")["href"])
# else:
#     print("wala")


# file = open("scrapesQuotes.csv", "w")
# writer = csv.writer(file)
# writer.writerow(["quotes", "authors"])

# for quote, author in zip(quotes, authors):
#     writer.writerow([quote.text,author.text])
# file.close()
