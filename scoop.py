# import libraries
import urllib.request
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import io
#remote+-%27not%2Bremote%27+-esl

def findRemote(scoop_page, queryo):
    # specify the url
    # scoop_page = scoop_page = "https://rochester.craigslist.org/search/jjj?query=remote+-'not+remote'"
    if "http://miami.craigslist.org/brw" in scoop_page:
        scoop_page = "https://miami.craigslist.org/search/brw/jjj?query="+queryo
    elif "http://miami.craigslist.org/mdc" in scoop_page:
        scoop_page = "https://miami.craigslist.org/search/mdc/jjj?query="+queryo
    elif "http://miami.craigslist.org/pbc" in scoop_page:
        scoop_page = "https://miami.craigslist.org/search/pbc/jjj?query="+queryo
    else:
        scoop_page = scoop_page + "search/jjj?query="+queryo
    print("Scoop URL" ,scoop_page)
    # query the website and return the html to the variable ‘page’
    page = urllib.request.urlopen(scoop_page)

    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')

    # Take out the <div> of name and get its value
    # Take out the <div> of name and get its value
    title_box = soup.find('a', attrs={'class': 'result-title'})
    count = 0
    with io.open('results.csv', 'a', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        for title_box in soup.find_all('a', attrs={'class': 'result-title'}):
            title = title_box.text.strip()  # strip() is used to remove starting and trailing
            print("Count: ", count, "Title", title, "Link: ", title_box['href'])
            count = count + 1

            writer.writerow([title, title_box['href'], datetime.now()])

