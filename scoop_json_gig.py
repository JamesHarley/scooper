import csv
import json

data = {}
data = {}  
data['gigs'] = []  

with open('gig_results.csv') as f:
	reader = csv.reader(f, delimiter=',')
	#csv rows
	for row in reader:
		if(not row): 
			continue
		print(row[0])
		data['gigs'].append({  
			'title': row[0],
			'link': row[1],
			'date':  row[2]
		})
			
	print(data)
	with open('gig_results.json', 'w') as outfile:  
		json.dump(data, outfile, indent=4)