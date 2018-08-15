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
			#print(total, " : ", a['href'])
			#seearchUSOnly
			if total < 420:
				scoop.findGigs(a['href'],'"build%2Bwebsite"%2B|%2B"build%2Bandroid"%2B|%2B"develop"%2B|%2B"wordpress"%2B|%2B"reactjs"%2B|%2B"react%2Bnative"+%2B+-uber+%2B+-lyft+-mover+-assistant+-coach+-landscape+-sales+-cleaner+-model+-marketing&is_paid=all')
			total = total + 1