import os
import csv
import pandas as pd 
class modelRun:
	def __init__(self):
		self.path = "/Users/changye.li/Documents/scripts/traitsPredictor/clean/"
	## get the list of all docs 
	# output: list that contains testing filenames
	def getDocs(self):
		docs = []
		for r, d ,f in os.walk(self.path):
			for files in f:
				if files.endswith(".csv"):
					docs.append(files)
		return docs
	## get attribute vector for each test user
	# output: normalized dataframe, which each entry represents user's attribute
	def processFiles(self):
		docs = self.getDocs()
		for each in docs:
			df = pd.read_csv(self.path + each)


## test
x = modelRun()
x.processFiles()