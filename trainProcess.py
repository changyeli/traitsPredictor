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
		self.better = pd.DataFrame()
		self.words = [] ## word to be analyzed
	## read all .csv file
	def readFiles(self):
		for r, d ,f in os.walk(self.root):
			for files in f:
				if files.endswith(".csv"):
					self.docs.append(files)
		self.better = pd.read_csv(self.path, header = None)
		self.words = list(self.better[0])
	## scan and analyze data by traits
	def processAGR(self):
		data = pd.read_csv(self.root + "cAGR.csv")
		status = list(data["STATUS"])
		stop = set(stopwords.words("english"))
		tokens = []
		for each in status:
			temp = [w for w in nltk.word_tokenize(each.translate(None, string.punctuation)) if not w in stop]
			tokens.append(temp)
		print tokens

## test
x = trainProcess()
x.readFiles()
x.processAGR()