## import packages
import os
import sklearn
import pandas as pd 
import numpy as np 
import nltk
import string
from nltk.corpus import stopwords
class trainProcess:
	def __init__(self):
		self.total = pd.DataFrame()
		self.path = "/Users/changye.li/Documents/scripts/traitsPredictor/process/better.csv"
		self.root = "/Users/changye.li/Documents/scripts/traitsPredictor/train/"
		self.docs = []
		self.better = pd.DataFrame() ## to store data
		self.vocal = {} ## reformat dataframe to dict
		self.words = [] ## word to be analyzed
		self.train = [] ## training data
		self.test = [] ## test data
	## read all .csv file
	def readFiles(self):
		for r, d ,f in os.walk(self.root):
			for files in f:
				if files.endswith(".csv"):
					self.docs.append(files)
		self.better = pd.read_csv(self.path, names = ['voculabury', 'anticipation', 'joy', 'negative', 'sadness', 'disgust', 'positive', 'anger', 'surprise', 'fear', 'trust'])
		self.words = list(self.better["voculabury"])
		self.vocal = self.better.set_index("voculabury").T.to_dict("list")
		print self.vocal
	## scan and process full dataset
	def processData(self):
		data = pd.read_csv(self.root + "cAGR.csv")
		status = list(data["STATUS"])
		stop = set(stopwords.words("english"))
		tokens = []
		## predined column names
		
		for each in status:
			## tokenize each status, remove all punctuations and lower the words
			temp = [w for w in nltk.word_tokenize(each.translate(None, string.punctuation).lower()) if not w in stop]
			## only keep the words that appear in the NRC list
			x = [w for w in temp if w in self.words]
			tokens.append(x)
			## treat all empty lists as zeros

## test
x = trainProcess()
x.readFiles()
x.processData()