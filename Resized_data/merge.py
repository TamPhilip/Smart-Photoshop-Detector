import pandas as pd

a = pd.read_csv("data.csv")
b = pd.read_csv("data2.csv")


import csv
with open('data.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row['image'])



# b = b.dropna(axis=1)
# merged = a.merge(b, on='title')
# merged.to_csv("output.csv", index=False)

