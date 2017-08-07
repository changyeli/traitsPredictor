## import packages
import os
import pandas as pd 
import nltk
import string
from nltk.corpus import stopwords
from sklearn.neural_network import MLPClassifier
from sklearn import svm
from sklearn.naive_bayes import BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
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
		self.matrix = [] ## normalized matrix layout for training data
		self.SVM = []
		self.MLP = []
		self.NB = []
		self.KNN = []
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
		temp = pd.DataFrame(temp)
		temp = np.divide((temp - np.mean(temp)), 15.)
		self.matrix = temp
	## train models
	def trainModel(self, filename, per):
		## randomly select train and test data
		train = self.matrix.sample(frac = per, replace = False)
		train_index = list(train.index)
		test_index = list(set(list(range(9917))) - set(train_index))
		test = pd.DataFrame(self.matrix, index = test_index)
		## retrieve class label 
		labels = pd.read_csv(self.root + filename, usecols = [1])
		labelTrain = pd.DataFrame(labels, index = train_index)
		labelTest = pd.DataFrame(labels, index = test_index)
		## dataframe to list
		labelTrain = labelTrain.values.tolist()
		labelTest = labelTest.values.tolist()
		## model fitting
		clf = MLPClassifier(activation = "logistic", solver = "adam", 
			alpha = 0.001, max_iter = 900000, hidden_layer_sizes = (150000, ))
		clf.fit(train, labelTrain)
		labelPredict = clf.predict(test)
		## find the correct predictions
		rate = [i for i, j in zip(labelPredict, labelTest) if i == j]
		print "MLP correct rate: ", float(len(rate))/float(len(labelPredict))
		self.MLP.append(float(len(rate))/float(len(labelPredict)))
		#######################################
		# SVM
		clf1 = svm.NuSVC(kernel = "sigmoid", nu = 0.3)
		clf1.fit(train, labelTrain)
		labelPredict1 = clf1.predict(test)
		rate1 = [i for i, j in zip(labelPredict1, labelTest) if i == j]
		print "SVM correct rate: ", float(len(rate1))/float(len(labelPredict1))
		self.SVM.append(float(len(rate1))/float(len(labelPredict1)))
		###########################################
		# Bernoulli naive bayes
		clf2 = BernoulliNB()
		clf2.fit(train, labelTrain)
		labelPredict2 = clf2.predict(test)
		rate2 = [i for i, j in zip(labelPredict2, labelTest) if i == j]
		print "Bernoulli Naive Bayes correct rate: ", float(len(rate2))/float(len(labelPredict2))
		self.NB.append(float(len(rate2))/float(len(labelPredict2)))
		###########################################
		# KNN
		clf3 = KNeighborsClassifier(n_neighbors = 10, weights = "distance")
		clf3.fit(train, labelTrain)
		labelPredict3 = clf3.predict(test)
		rate3 = [i for i, j in zip(labelPredict3, labelTest) if i == j]
		print "KNN correct rate: ", float(len(rate3))/float(len(labelPredict3))
		self.KNN.append(float(len(rate2))/float(len(labelPredict2)))
		

## test
x = trainProcess()
x.readFiles()
tokens = x.processData()
x.getAttr(tokens)
for i in range(100):
	print "This is ", i, "iteration."
	for f in x.docs:
		print "processing ", f
		x.trainModel(f, 0.9)

print "MLP average correct rate: ", sum(x.MLP)/len(x.MLP)
print "SVM average correct rate: ", sum(x.SVM)/len(x.SVM)
print "NB average correct rate: ", sum(x.NB)/len(x.NB)
print "KNN average correct rate:", sum(x.KNN)/len(x.KNN)