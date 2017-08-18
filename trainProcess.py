## import packages
import pandas as pd 
import numpy as np 
import pickle
from sklearn.neural_network import MLPClassifier
from sklearn import linear_model
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_val_score
class trainProcess:
	def __init__(self):
		self.data = pd.read_csv("/Users/changye.li/Documents/scripts/traitsPredictor/clean/trainV2.csv")
		self.label = [15, 16, 17, 18, 19] ## labeled traits column indexes
		self.score = [10, 11, 12, 13, 14] ## scored traits column indexes
		self.train = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] ## train data column indexes
		## the labeled traits are [cEXT, cNEU, cAGR, cCON, cOPN] -> [15, 16, 17, 18, 19]
		## the scored traits are [sECT, sNEU, sAGR, sCON, sOPN] -> [10, 11, 12, 13, 14]
	## training model process, classification
	def trainModelLabel(self):
		sample = self.data.iloc[:, self.train]
		name = ["ext", "neu", "agr", "con", "opn"]
		## iterate each trait
		for trait in self.label:
			label = self.data.iloc[:, trait]
			print "processing trait: ", name[self.label.index(trait)]
			############################################################
			## SGD
			clf = linear_model.SGDClassifier(loss = "log", penalty = "elasticnet")
			scores = cross_val_score(clf, sample, label, cv = 10, scoring = "f1")
			print("SGD Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
			############################################################
			## Random Forest
			clf = RandomForestClassifier(criterion = "entropy", n_estimators = 30)
			scores = cross_val_score(clf, sample, label, cv = 10, scoring = "f1")
			print("Random Forest Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
			###########################################################
			## multinomial nb
			clf = MultinomialNB()
			scores = cross_val_score(clf, sample, label, cv = 10)
			print("Multinomial NB Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
			##########################################################
			## bernoulli nb
			clf = BernoulliNB()
			scores = cross_val_score(clf, sample, label, cv = 10)
			print("Bernoulli NB Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
			#########################################################
			## gradient tree boosting
			clf = GradientBoostingClassifier(loss = "deviance", n_estimators = 200, criterion = "mse")
			scores = cross_val_score(clf, sample, label, cv = 10)
			print("Gradient Boosting Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

			print "\n"
	## TODO: training model process, regression
	
		
x = trainProcess()
x.trainModelLabel()