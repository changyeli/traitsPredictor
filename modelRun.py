import os
import pickle
import pandas as pd
from trainProcess import trainProcess
class modelRun:
	def __init__(self):
		self.path = "/Users/changye.li/Documents/scripts/traitsPredictor/process/"
		self.label_model = {} ## to store classfication model
		self.modelYes = {} ## to store regression "yes" model
		self.modelNo = {} ## to store regression "no" model
		self.name = [] ## trait names
	## get the list of all docs 
	## output: list that contains testing filenames
	def getDocs(self):
		docs = []
		for r, d ,f in os.walk(self.path):
			for files in f:
				if files.endswith(".csv") and files != "better.csv":
					docs.append(files)
		return docs
	## get trained model
	## output: update dict to store trained model
	def getModel(self):
		m = trainProcess()
		self.name = m.name
		self.label_model = m.trainModelLabel()
		m.saveModel()
		self.modelYes = m.modelYes
		self.modelNo = m.modelNo
	## apply trained model on validation dataset
	## user: user processed data to scan, gathered from getDocs
	def getTrained(self, user):
		s = self.path + user
		dt = pd.read_csv(s)
		for item in self.name:
			pre = pickle.loads(self.label_model[item]).predict(dt)
			print pre
	## TODO: get regression socres based on classified label
	## TODO: group all scores
x = modelRun()
x.getModel()
x.getTrained("BillGates.csv")