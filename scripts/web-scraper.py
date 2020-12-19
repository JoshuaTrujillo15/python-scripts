# web scraper bot
# DO NOT USE THIS WITHOUT THE WEBSITE'S PERMISSION
# check robots.txt file for more info (www.example.com/robots.txt)

import requests
import bs4
import re
import time

def getTitle(soup):
    title = soup.title
    return title

def getLinks(soup):
    link_array = []
    links = soup.find_all('a', href=True)

    for link in links:
        link_array.append(link["href"])
    
    return link_array

def main():
    
    #start timer
    start_time = time.time()

    url = "" # insert url of site to scrape

    html = requests.get(url)
    soup = bs4.BeautifulSoup(html.text, 'html.parser')

    title = getTitle(soup)
    link_array = getLinks(soup)

    print(title)
    print(link_array)

    #end timer
    run_time = time.time() - start_time
    print("Executed without error in {} seconds".format(run_time))

if __name__ == "__main__":
    main()