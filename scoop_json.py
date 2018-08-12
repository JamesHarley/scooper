import pandas as pd

def scoopJSON(csvPath,jsonPath):
	csv_file = pd.DataFrame(pd.read_csv(csv, sep = ",", header = 0, index_col = False))
	csv_file.to_json(jsonPath, orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None