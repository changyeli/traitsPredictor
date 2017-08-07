## import packages
import os
import pandas as pd 
import nltk
import string
import sklearn
import numpy as np 
from operator import add
from nltk.corpus import stopwords
class trainRegression:
	def __init__(self):
		## path of vocabulary list in better format
		self.path = "/Users/changye.li/Documents/scripts/traitsPredictor/process/better.csv"
		## train dataset path
		self.files = "/Users/changye.li/Documents/scripts/traitsPredictor/mypersonality_final.csv"
		## data frame that contains all processed status
		## each entry represents word count of each user
		self.processed = []
		## vocabulary list in better format, with attributes
		self.better = pd.DataFrame()
		## vocabulary list
		self.voca = []
		self.dic = {}
		## all unprocessed data
		self.data = pd.DataFrame()
	## read files
	def readFiles(self):
		self.better = pd.read_csv(self.path, names = ['voculabury', 'anticipation', 'joy', 'negative', 'sadness', 'disgust', 'positive', 'anger', 'surprise', 'fear', 'trust'])
		self.voca = self.better["voculabury"].values.tolist()
		self.dic = self.better.set_index("voculabury").T.to_dict("list")
		self.data = pd.read_csv(self.files)
	## data processing
	def process(self):
		## user ID
		uid = set(self.data["AUTHID"].values.tolist())
		## iterate each user
		for id in uid:
			## store each user's processed status update
			tokens = []
			## subset dataset
			k1 = self.data[self.data["AUTHID"] == id]
			## retrieve user's status update
			s1 = k1["STATUS"].values.tolist()
			## iterate each status update 
			for each in s1:
				## remove punctuation
				temp = [w for w in nltk.word_tokenize(each.translate(None, string.punctuation).lower())]
				## remove stopwords
				x = [w for w in temp if w in self.voca]
				tokens.append(x)
			## store attributes of each user's processed status update
			temp = []
			## iterate each status update
			for each in tokens:
				attr = [0]*10
				if len(each) == 0: ## empty list
					temp.append(attr)
				else:
					## iterate each word in status
					for item in each:
						attr = [x + y for x, y in zip(attr, self.dic[item])]
					temp.append(attr)
			## element-wise addtion among list of lists
			self.processed.append([sum(x) for x in zip(*temp)])
## test
x = trainRegression()
x.readFiles()
x.process()