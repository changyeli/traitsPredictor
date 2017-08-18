import os
import csv
import pickle
import pandas as pd
from sklearn import preprocessing
from trainProcess import trainProcess
from trainBuild import trainBuild
from sklearn.model_selection import cross_val_predict
class modelRun:
	def __init__(self):
		self.path = "/Users/changye.li/Documents/scripts/traitsPredictor/pross/"
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
	# output: integrated dataset
	def processFiles(self):
		docs = self.getDocs()
		attr = []
		for each in docs:
			print "processing file: ", each
			df = pd.read_csv(self.path + each)
			attr.append(df.sum(axis = 0).values.tolist())
		attr = pd.DataFrame(attr)
		## normalization
		attr = preprocessing.normalize(attr)
		return attr
x = modelRun()
print x.processFiles()