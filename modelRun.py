import os
import csv
import pandas as pd 
from sklearn import preprocessing
from trainProcess import trainProcess
from trainBuild import trainBuild
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
		attr = []
		for each in docs:
			print "processing file: ", each
			df = pd.read_csv(self.path + each)
			attr.append(df.sum(axis = 0).values.tolist())
		attr = pd.DataFrame(attr)
		## normalization
		attr = preprocessing.normalize(attr)
		return attr
	## get prediction from trained model
	# output: list of five list, which each sublist is the predicted label for each trait
	def getLabel(self):
		attr = self.processFiles()
		traits = ["EXT", "NEU", "AGR", "CON", "OPN"]
		pre = [] ## store predictions for each trait
		## get trained model
		x = trainProcess()
		files = x.readFiles()
		tokens = x.processData()
		df = x.getAttr(tokens)
		models = x.getModel(files, df)
		## get prediction
		for item in traits:
			p = models[item].predict(attr).values.tolist()
			pre.append(p)
		print pre
	## get scores from training data
	# output: user scores for each trait
	def getScore(self):
		y = trainBuild()
		y.readFiles()
		df1 = y.process()
		score = y.group(df1)



## test
x = modelRun()
x.getLabel()