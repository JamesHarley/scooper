# import libraries
import urllib.request
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import io
import json

def findRemote(scoop_page, queryo):
	# specify the url
	# scoop_page = scoop_page = "https://rochester.craigslist.org/search/jjj?query=remote+-'not+remote'"
	if "http://miami.craigslist.org/brw" in scoop_page:
		scoop_page = "https://miami.craigslist.org/search/brw/jjj?query="+queryo+"&postedToday=1&bundleDuplicates=1"
	elif "http://miami.craigslist.org/mdc" in scoop_page:
		scoop_page = "https://miami.craigslist.org/search/mdc/jjj?query="+queryo+"&postedToday=1&bundleDuplicates=1"
	elif "http://miami.craigslist.org/pbc" in scoop_page:
		scoop_page = "https://miami.craigslist.org/search/pbc/jjj?query="+queryo+"&postedToday=1&bundleDuplicates=1"
	else:
		scoop_page = scoop_page + "search/jjj?query="+queryo+"&postedToday=1&&bundleDuplicates=1"
	print("Scoop URL" ,scoop_page)
	# query the website and return the html to the variable ‘page’
	page = urllib.request.urlopen(scoop_page)

	# parse the html using beautiful soup and store in variable `soup`
	soup = BeautifulSoup(page, 'html.parser')

	# Take out the <div> of name and get its value
	# Take out the <div> of name and get its value
	title_box = soup.find('a', attrs={'class': 'result-title'})
	count = 0
	with io.open('remote_results.csv', 'a', encoding="utf-8") as csv_file:
		writer = csv.writer(csv_file)
		for title_box in soup.find_all('a', attrs={'class': 'result-title'}):
			title = title_box.text.strip()  # strip() is used to remove starting and trailing
			
			#check for duplicates
			with open('remote_results.csv') as f:
				reader = csv.reader(f)
				duplicate = False
				for row in reader:
					check =  (title_box['href'],title)
					if  any (s in row for s in check):
						print ("###############DUPLICATE FOUND################")
						duplicate = True
				#end check
			print("Count: ", count, "Title", title, "Link: ", title_box['href'])
			count = count + 1
			if duplicate == False:
				writer.writerow([title, title_box['href'], datetime.now()])
				

def findGigs(scoop_page, queryo):
	# specify the url
	if "http://miami.craigslist.org/brw" in scoop_page:
		scoop_page = "https://miami.craigslist.org/search/ggg?query="+queryo+"&postedToday=1&bundleDuplicates=1"
	elif "http://miami.craigslist.org/mdc" in scoop_page:
		scoop_page = "https://miami.craigslist.org/search/ggg?query="+queryo+"&postedToday=1&bundleDuplicates=1"
	elif "http://miami.craigslist.org/pbc" in scoop_page:
		scoop_page = "https://miami.craigslist.org/search/ggg?query="+queryo+"&postedToday=1&bundleDuplicates=1"
	else:
		scoop_page = scoop_page + "search/ggg?query="+queryo+"&postedToday=1&bundleDuplicates=1"
	print("Scoop URL" ,scoop_page)
	# query the website and return the html to the variable ‘page’
	page = urllib.request.urlopen(scoop_page)

	# parse the html using beautiful soup and store in variable `soup`
	soup = BeautifulSoup(page, 'html.parser')

	# Take out the <div> of name and get its value
	# Take out the <div> of name and get its value
	title_box = soup.find('a', attrs={'class': 'result-title'})
	count = 0
	with io.open('gig_results.csv', 'a', encoding="utf-8") as csv_file:
		writer = csv.writer(csv_file)
		for title_box in soup.find_all('a', attrs={'class': 'result-title'}):
			title = title_box.text.strip()  # strip() is used to remove starting and trailing
			#check for duplicates
			with open('gig_results.csv') as f:
				reader = csv.reader(f)
				duplicate = False
				for row in reader:
					check =  (title_box['href'],title)
					if  any (s in row for s in check):
						print ("###############DUPLICATE FOUND################")
						duplicate = True
				#end check
			print("Count: ", count, "Title", title, "Link: ", title_box['href'])
			count = count + 1
			if duplicate == False:
				writer.writerow([title, title_box['href'], datetime.now()])