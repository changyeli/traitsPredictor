## import packages
import os
import pandas as pd 
import nltk
import string
from nltk.corpus import stopwords
from sklearn.neural_network import MLPClassifier
from sklearn import svm
import numpy as np 
class trainProcess:
	def __init__(self):
		self.total = pd.DataFrame()
		self.path = "/Users/changye.li/Documents/scripts/traitsPredictor/process/better.csv"
		self.root = "/Users/changye.li/Documents/scripts/traitsPredictor/train/"
		self.docs = []
		self.better = pd.DataFrame() ## to store data
		self.vocal = {} ## reformat dataframe to dict, voculabury as key, attributes as values
		self.words = [] ## word to be analyzed
		self.train = [] ## training data
		self.test = [] ## test data
		self.matrix = [] ## matrix layout for training data
	## read all .csv file
	# output: tokenized word for each status update
	def readFiles(self):
		for r, d ,f in os.walk(self.root):
			for files in f:
				if files.endswith(".csv"):
					self.docs.append(files)
		## with column name
		self.better = pd.read_csv(self.path, names = ['voculabury', 'anticipation', 'joy', 'negative', 'sadness', 'disgust', 'positive', 'anger', 'surprise', 'fear', 'trust'])
		self.words = list(self.better["voculabury"])
		self.vocal = self.better.set_index("voculabury").T.to_dict("list")
	## scan and process full dataset
	def processData(self):
		data = pd.read_csv(self.root + "cAGR.csv")
		status = list(data["STATUS"])
		stop = set(stopwords.words("english"))
		tokens = []
		## predined column names
		for each in status:
			## tokenize each status, remove all punctuations, stopwords and lower the words
			temp = [w for w in nltk.word_tokenize(each.translate(None, string.punctuation).lower()) if not w in stop]
			## only keep the words that appear in the NRC list
			x = [w for w in temp if w in self.words]
			tokens.append(x)
		return tokens
			## treat all empty lists as zeros
	## reformat data into matrix layout, each status is a 10-dimensional vector, 
	## with adding each word's attribute to corresponding column
	# input: pre-processed tokenized words (list of lists) from processData function
	def getAttr(self, values):
		temp = [] ## temporary data storage
		## every status update
		for each in values:
			attr = [0] *10 ## feature vector
			## empty list
			if len(each) == 0:
				temp.append(attr)
			else:
				## each word in a status update:
				for item in each:
					attr = [x + y for x, y in zip(attr, self.vocal[item])]
				temp.append(attr)
		## normalize matrix, follow central limit theroem
		temp = np.matrix(temp)
		temp = (temp - np.mean(temp))/temp.var()
		self.matrix = temp
	## get training and test data, 80% of data as training data, and the rest as test data
	def sliceData(self):
		sample = int(len(self.matrix)* 0.8)
		self.train = self.matrix[:sample]
		self.test = self.matrix[sample:]
	## MLP training for AGR
	def MLPtrain_AGR(self):
		## take label column and reformat to list
		labels = pd.read_csv(self.root + "cAGR.csv", usecols = [1]).values.tolist()
		## slice training and test labels
		sample = int(len(self.matrix) *0.8)
		labelTrain = labels[:sample]
		labelTest = labels[sample:]
		self.train[:, 11] = labelTrain
		print self.train

## test
x = trainProcess()
x.readFiles()
tokens = x.processData()
x.getAttr(tokens)
x.sliceData()
x.MLPtrain_AGR()