## import packages
import os
import pandas as pd 
import nltk
import string
import sklearn
import numpy as np 
from operator import add
from nltk.corpus import stopwords
from sklearn import preprocessing
class trainBuild:
	def __init__(self):
		## path of vocabulary list in better format
		self.path = "/Users/changye.li/Documents/scripts/traitsPredictor/process/better.csv"
		## train dataset path
		self.files = "/Users/changye.li/Documents/scripts/traitsPredictor/mypersonality_final.csv"
		## data frame that contains all processed status
		## each entry represents word count of each user
		self.processed = pd.DataFrame()
		## vocabulary list in better format, with attributes
		self.better = pd.DataFrame()
		## vocabulary list
		self.voca = []
		self.dic = {}
		## all unprocessed data
		self.data = pd.DataFrame()
		## attribute name
		self.attr = ['voculabury', 'anticipation', 'joy', 'negative', 'sadness', 'disgust', 'positive', 'anger', 'surprise', 'fear', 'trust']
		self.values = ["sEXT", "sNEU", "sAGR", "sCON", "sOPN", "cEXT", "c0EU", "cAGR", "cCON", "cOPN"]
	## read files
	def readFiles(self):
		self.better = pd.read_csv(self.path, names = self.attr)
		self.voca = self.better["voculabury"].values.tolist()
		self.dic = self.better.set_index("voculabury").T.to_dict("list")
		self.data = pd.read_csv(self.files)
	## data processing
	def process(self):
		process = []
		## user ID
		uid = set(self.data["AUTHID"].values.tolist())
		stop = set(stopwords.words("english"))
		## iterate each user
		for id in uid:
			## store each user's processed status update
			tokens = []
			## subset dataset
			k1 = self.data[self.data["AUTHID"] == id]
			t = k1[k1.columns[-10:]].iloc[0].values.tolist()
			## retrieve user's status update
			s1 = k1["STATUS"].values.tolist()
			## iterate each status update 
			for each in s1:
				## remove punctuation
				temp = [w for w in nltk.word_tokenize(each.translate(None, string.punctuation).lower()) if not w in stop]
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
			temp_scaled = preprocessing.normalize(temp)
			## element-wise addtion among list of lists
			process.append([sum(x) for x in zip(*temp_scaled)] + k1[k1.columns[-10:]].iloc[0].values.tolist())
			## reformat into new and processed dataframe
		process = pd.DataFrame(process, columns = self.attr[1:] + self.values)
		#process.to_csv("processed_data.csv", index = False)
		return process
	## only keep median if |median - mean| <=0.09
	# input: dataframe that only contains trait score
	# output: dict, with trait as key, all median as values
	def compare(self, df):
		group = {}
		df = df[df.cEXT == 1]
		temp = df.iloc[:, 10:15]
		s1 = temp.median(axis = 0)
		s2 = temp.mean(axis = 0)
		s = pd.concat([s1, s2], axis = 1)
		print s
		print s[0].values.tolist()
## test
x = trainBuild()
x.readFiles()
df = x.process()
x.compare(df)