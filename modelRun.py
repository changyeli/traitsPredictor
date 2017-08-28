import os
import pickle
import pandas as pd
import numpy as np
from trainProcess import trainProcess
from scipy.stats import mode
class modelRun:
	def __init__(self):
		self.path = "/Users/changye.li/Documents/scripts/traitsPredictor/process/"
		self.root = "/Users/changye.li/Documents/scripts/traitsPredictor/predict/"
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
	## user: user's processed data to scan, gathered from getDocs
	def getTrained(self, user):
		s = self.path + user
		dt = pd.read_csv(s)
		pred = []
		for item in self.name:
			print "processing trait:", item
			pre = pickle.loads(self.label_model[item]).predict(dt).tolist()
			pred.append(pre)
			print mode(pre), len(pre)
		pred = np.matrix(np.array(pred))
		mat = pd.concat([dt, pd.DataFrame(pred.transpose())], axis = 1)
		mat.columns = ['anticipation', 'joy', 'negative', 'sadness', 
			'disgust', 'positive', 'anger', 'surprise', 'fear', 'trust',
			'ext', 'neu', 'agr', 'con', 'opn']
		## write to file
		s1 = self.root + user
		mat.to_csv(s1, index = False)
		print "Finish writing to file"
	## TODO: get regression socres based on classified label
	## apply regression model on classified dataset
	## user: validation user's processed data to scan, gathered from getDocs
	def getRegressed(self, user):
		s = self.root + user
		df = pd.read_csv(s)
		for item in self.name:
			item = item.upper()
		print df[df.EXT == 1].ix[:, :"trust"]
	## TODO: group all scores
x = modelRun()
docs = x.getDocs()
x.getModel()
for files in docs:
	print "processing validation user file: ", files
	x.getTrained(files)
	print "\n"