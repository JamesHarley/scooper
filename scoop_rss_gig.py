from bs4 import BeautifulSoup
import urllib.request
import scoop
from datetime import datetime
import csv
import io
import pandas as pd
from json2html import *
import json



scoop_page = 'https://www.craigslist.org/about/sites'
# query the website and return the html to the variable ‘page’
page = urllib.request.urlopen(scoop_page)

soup = BeautifulSoup(page, 'html.parser')

count = 0
total = 1

with io.open('rss_gig.csv', 'a', encoding="utf-8") as csv_file:
	writer = csv.writer(csv_file)
	for a in soup.find_all('a', href=True):
		if count < 7:
			count = count + 1
		else:
			if total < 714:
				print(total, " : ", a['href'])
				#seearchUSOnly
				if total < 420:
					ab = a['href']
					row = a['href']+'/search/jjj?format=rss&query=\'build%2Bwebsite\'%2B|%2B\'build%2Bandroid\'%2B|%2B\'develop\'%2B|%2B\'wordpress\'%2B|%2B\'reactjs\'%2B|%2B\'react%2Bnative\'+%2B+-uber+%2B+-lyft+-mover+-assistant+-coach+-landscape+-sales+-cleaner+-model+-marketing&is_paid=all'
					writer.writerow(['<a href="'+row+'">'+ab+'</a>'])
				total = total + 1
	csv_file = pd.DataFrame(pd.read_csv('rss_gig.csv', sep = ",", header = 0, index_col = False))
	csv_file.to_json('rss_gig.json', orient = "table", date_format = "iso")
	
	data = open('rss_gig.json','r')
	jsonFile = data.read()
	foo = json.loads(jsonFile)
	table_attr = {"style" : "width:100%", "class" : "table table-striped"}
	html = json2html.convert(foo,table_attributes=table_attr)

	with io.open("rss_gig.html", "w", encoding="utf-8") as ht:
		ht.write(html)