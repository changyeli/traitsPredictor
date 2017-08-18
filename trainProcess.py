## import packages
import pandas as pd 
import numpy as np 
import pickle
from sklearn.neural_network import MLPClassifier
from sklearn import linear_model
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
class trainProcess:
	def __init__(self):
		self.attr = ['voculabury', 'anticipation', 'joy', 'negative', 'sadness', 'disgust', 'positive', 'anger', 'surprise', 'fear', 'trust']
	## training model process, with integrated dataset
	# input: trait name
	# output: evaluation scores
	def trainModelIntegrated(self, trait):
		processed_data = pd.read_csv("/Users/changye.li/Documents/scripts/traitsPredictor/processed_data.csv")
		sample = processed_data.loc[:, self.attr[1:]]
		label = processed_data.loc[:, trait]
		########################################################
		## SGD 
		clf = linear_model.SGDClassifier(loss = "log", penalty = "elasticnet")
		scores = cross_val_score(clf, sample, label, cv = 10, scoring = "f1")
		print("SGD Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
		########################################################
		## MLP
		clf = MLPClassifier(solver = "adam", 
			alpha = 0.001, max_iter = 90000, hidden_layer_sizes = (1500, 10))
		scores = cross_val_score(clf, sample, label, cv = 10, scoring = "f1")
		print("MLP Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
		#######################################################
		## tree
		clf = tree.DecisionTreeClassifier(criterion = "gini", splitter = "random", max_features = "sqrt")
		scores = cross_val_score(clf, sample, label, cv = 10, scoring = "f1")
		print("Dscision Tree Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
		#######################################################
		## Bernoulli naive bayes
		clf = RandomForestClassifier(criterion = "gini", n_estimators = 15)
		scores = cross_val_score(clf, sample, label, cv = 10, scoring = "f1")
		print("Random Forest Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
	def trainModel(self, trait):
		
x = trainProcess()
x.trainModelIntegrated()