from bs4 import BeautifulSoup
import urllib.request
import scoop
from datetime import datetime

scoop_page = 'https://www.craigslist.org/about/sites'
# query the website and return the html to the variable ‘page’
page = urllib.request.urlopen(scoop_page)

soup = BeautifulSoup(page, 'html.parser')

count = 0
total = 1
for a in soup.find_all('a', href=True):
    if count < 7:
        count = count + 1
    else:
        if total < 714:
            print(total, " : ", a['href'])
			#seearchUSOnly
            if total < 420:
                # remote+-%27not%2Bremote%27+-esl
				scoop.findRemote(a['href'],"remote+-not+remote+java+|+javascript+|+web+developer++|+android+developer+|++programmer+|+wordpress+|+developer")
				#scoop.findGigs(a[href],'"build+website"+|+"build+android"+|+"develop"+|+"developer"+|+"wordpress"+|+"reactjs"+|+"react+native"&is_paid=all')
            total = total + 1