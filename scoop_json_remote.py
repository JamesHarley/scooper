import csv
import json

data = {}
data = {}  
data['remote'] = []  

with open('remote_results.csv') as f:
	reader = csv.reader(f, delimiter=',')
	#csv rows
	for row in reader:
		if(not row): 
			continue
		print(row[0])
		data['remote'].append({  
			'title': row[0],
			'link': row[1],
			'date':  row[2]
		})
			
	print(data)
	with open('../remote_results.json', 'w') as outfile:  
		json.dump(data, outfile, indent=4)