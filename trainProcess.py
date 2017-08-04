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
		## normalize matrix
		temp = np.matrix(temp)
		temp = np.divide((temp - np.mean(temp)), 15.)
		self.matrix = temp
		
		return 
	## process AGR data
	def AGR(self, per):
		sample = int(len(self.matrix)* per)
		self.train = self.matrix[:sample]
		self.test = self.matrix[sample:]
		sample = int(len(self.matrix) * per)
		#####################################
		# MLP
		## take label column and reformat to list
		labels = pd.read_csv(self.root + "cAGR.csv", usecols = [1])
		## slice training and test labels
		labelTrain = labels[:sample]
		labelTest = labels[sample:]
		clf = MLPClassifier(activation = "logistic", solver = "adam", alpha = 0.001, max_iter = 200000, hidden_layer_sizes = (50000, ))
		clf.fit(self.train, labelTrain.values.ravel())
		labelPredict = clf.predict(self.test)
		## find the correct predictions
		rate = [i for i, j in zip(labelPredict, labelTest.as_matrix()) if i == j]
		print "MLP correct rate: ", float(len(rate))/float(len(labelPredict))
		#######################################
		# SVM
		clf1 = svm.NuSVC(kernel = "sigmoid")
		clf1.fit(self.train, labelTrain.values.ravel())
		labelPredict1 = clf1.predict(self.test)
		rate1 = [i for i, j in zip(labelPredict1, labelTest.as_matrix()) if i == j]
		print "SVM correct rate: ", float(len(rate1))/float(len(labelPredict1))

## test
x = trainProcess()
x.readFiles()
tokens = x.processData()
x.getAttr(tokens)
x.AGR(0.9)
