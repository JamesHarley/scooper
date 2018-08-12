import pandas as pd

#def scoopJSON(csvPath,jsonPath):
csv_file = pd.DataFrame(pd.read_csv('gig_results.csv', sep = ",", header = 0, index_col = False))
csv_file.to_json('gig_results.json', orient = "table", date_format = "iso")