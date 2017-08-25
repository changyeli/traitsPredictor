import os
import pickle
from trainProcess import trainProcess
class modelRun:
	def __init__(self):
		self.path = "/Users/changye.li/Documents/scripts/traitsPredictor/process/"
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
	def getModel(self):
		m = trainProcess()
		label_model = m.trainModelLabel()
		m.saveModel()
		modelYes = m.modelYes
		modelNo = m.modelNo
x = modelRun()
x.getModel()