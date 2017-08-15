## import packages
import os
import pandas as pd 
import nltk
import string
import operator
from nltk.corpus import stopwords
from sklearn.neural_network import MLPClassifier
from sklearn import svm
from sklearn.naive_bayes import BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_predict
from sklearn import metrics
from sklearn import preprocessing
import numpy as np 
class trainProcess:
	def __init__(self):
		self.total = pd.DataFrame()
		self.path = "/Users/changye.li/Documents/scripts/traitsPredictor/process/better.csv"
		self.root = "/Users/changye.li/Documents/scripts/traitsPredictor/train/"
		self.better = pd.DataFrame() ## to store data
		self.vocal = {} ## reformat dataframe to dict, voculabury as key, attributes as values
		self.words = [] ## word to be analyzed
		self.attr = ['voculabury', 'anticipation', 'joy', 'negative', 'sadness', 'disgust', 'positive', 'anger', 'surprise', 'fear', 'trust']
	## read all .csv file
	# output: tokenized word for each status update
	def readFiles(self):
		docs = []
		for r, d ,f in os.walk(self.root):
			for files in f:
				if files.endswith(".csv"):
					docs.append(files)
		## with column name
		self.better = pd.read_csv(self.path, names = self.attr)
		self.words = list(self.better["voculabury"])
		self.vocal = self.better.set_index("voculabury").T.to_dict("list")
		return docs
	## scan and process full dataset
	def processData(self):
		data = pd.read_csv(self.root + "cAGR.csv")
		status = list(data["STATUS"])
		tokens = []
		stop = set(stopwords.words("english"))
		## predined column names
		for each in status:
			## tokenize each status, remove all punctuations, stopwords and lower the words
			temp = [w for w in nltk.word_tokenize(each.translate(None, string.punctuation).lower())if not w in stop]
			## only keep the words that appear in the NRC list
			x = [w for w in temp if w in self.words]
			tokens.append(x)
		return tokens
			## treat all empty lists as zeros
	## reformat data into matrix layout, each status is a 10-dimensional vector, 
	## with adding each word's attribute to corresponding column
	# input: pre-processed tokenized words (list of lists) from processData function
	# output: processed dataframe
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
		temp = pd.DataFrame(temp)
		temp = preprocessing.normalize(temp)
		temp = pd.DataFrame(temp)
		return temp
	## training model process
	# input: processed dataframe, file to be read
	# output: prediction scores by cross validation
	def trainModel(self, df, filename):
		## add label column
		df.columns = self.attr[1:]
		label = pd.read_csv(self.root + filename, usecols = [1])
		df = df.assign(label = label.values)
		df.to_csv("test.csv")
		####################################
		# MLP
		clf = MLPClassifier(activation = "logistic", solver = "adam", 
			alpha = 0.001, max_iter = 90000, hidden_layer_sizes = (15000, ))
		predicted = cross_val_predict(clf, df[self.attr[1:]], df["label"], cv = 10)
		print "MLP CV score: ", metrics.accuracy_score(df["label"], predicted)
		####################################
		# SVM
		clf1 = svm.NuSVC(kernel = "sigmoid", nu = 0.3)
		predicted = cross_val_predict(clf1, df[self.attr[1:]], df["label"], cv = 10)
		print "SVM CV score: ", metrics.accuracy_score(df["label"], predicted)
		###########################################
		# Bernoulli naive bayes
		clf2 = BernoulliNB()
		predicted = cross_val_predict(clf2, df[self.attr[1:]], df["label"], cv = 10)
		print "NB CV score: ", metrics.accuracy_score(df["label"], predicted)
		####################################
		# KNN
		clf3 = KNeighborsClassifier(n_neighbors = 10, weights = "distance")
		predicted = cross_val_predict(clf3, df[self.attr[1:]], df["label"], cv = 10)
		print "KNN CV score: ", metrics.accuracy_score(df["label"], predicted)

		## export trained model
		if(filename == "cAGR.csv"):
			return clf
		else:
			return clf2
	def getModel(self, docs, df):
		models = []
		for item in docs:
			print "Process file:  ", item
			models.append(self.trainModel(df, item))
		return models
