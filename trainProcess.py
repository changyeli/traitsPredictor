import pandas
import pickle
from sklearn import linear_model
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier, RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error,make_scorer
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor, MLPClassifier
class trainProcess:
	def __init__(self):
		self.data = pandas.read_csv("/Users/changye.li/Documents/scripts/traitsPredictor/clean/trainV2.csv")
		self.label = [15, 16, 17, 18, 19] ## labeled traits column indexes
		self.score = [10, 11, 12, 13, 14] ## scored traits column indexes
		self.train = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] ## train data column indexes
		self.modelYes = {}
		self.modelNo = {}
		self.name = ["ext", "neu", "agr", "con", "opn"]
		## the labeled traits are [cEXT, cNEU, cAGR, cCON, cOPN] -> [15, 16, 17, 18, 19]
		## the scored traits are [sECT, sNEU, sAGR, sCON, sOPN] -> [10, 11, 12, 13, 14]
	## training model process, classification
	## store the best model
	## input: trait name, label status
	## output: the best-fitted model for each trait
	def trainModelLabel(self):
		sample = self.data.iloc[:, self.train]
		s = {} ## best model for each trait, with trait name as key, model as value
		## iterate each trait
		for trait in self.label:
			result = {} ## validation result
			models = {} ## store best-fitting model
			label = self.data.iloc[:, trait]
			print "processing trait: ", self.name[self.label.index(trait)]
			############################################################
			## SGD
			clf = linear_model.SGDClassifier(loss = "log", penalty = "elasticnet")
			clf.fit(sample, label)
			scores = cross_val_score(clf, sample, label, cv = 5, scoring = "f1")
			print("SGD Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
			result["SGD"] = scores.mean()
			models["SGD"] = pickle.dumps(clf)
			############################################################
			## Random Forest
			clf = RandomForestClassifier(criterion = "entropy", n_estimators = 30)
			clf.fit(sample, label)
			scores = cross_val_score(clf, sample, label, cv = 5, scoring = "f1")
			print("Random Forest Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
			result["RF"] = scores.mean()
			models["RF"] = pickle.dumps(clf)
			###########################################################
			## multinomial nb
			clf = MultinomialNB()
			clf.fit(sample, label)
			scores = cross_val_score(clf, sample, label, cv = 5)
			print("Multinomial NB Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
			result["MNB"] = scores.mean()
			models["MNB"] = pickle.dumps(clf)
			##########################################################
			## bernoulli nb
			clf = BernoulliNB()
			clf.fit(sample, label)
			scores = cross_val_score(clf, sample, label, cv = 5)
			print("Bernoulli NB Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
			result["BNB"] = scores.mean()
			models["BNB"] = pickle.dumps(clf)
			#########################################################
			## gradient tree boosting
			clf = GradientBoostingClassifier(loss = "deviance", n_estimators = 200, criterion = "mse")
			clf.fit(sample, label)
			scores = cross_val_score(clf, sample, label, cv = 5)
			print("Gradient Boosting Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
			result["GB"] = scores.mean()
			models["GB"] = pickle.dumps(clf)
			#########################################################
			## MLP
			clf = MLPClassifier(hidden_layer_sizes = (500,), learning_rate = "invscaling", max_iter = 1000)
			clf.fit(sample, label)
			scores = cross_val_score(clf, sample, label, cv = 5)
			print("MLP Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
			result["GB"] = scores.mean()
			models["GB"] = pickle.dumps(clf)
			print "\n"

			## find the highest f1 score and associated model, store it to output dict
			h = max(result, key = result.get)
			s[self.name[self.label.index(trait)]] = pickle.dumps(pickle.loads(models[h]))
		return s
	## training model process, regression
	## input: trait name
	## label status: y for yes (1), n for no (0)
	## output: the best-fitting model
	def trainModelRegression(self, trait, status):
		root = "/Users/changye.li/Documents/scripts/traitsPredictor/clean/"
		file_name = trait.lower() + status.upper() + ".csv"
		sample = pandas.read_csv(root + file_name)
		name = "s" + trait.upper()
		dt = pandas.read_csv(root + file_name)
		sample = dt.iloc[:, 0:10]
		label = dt[[name]]
		## evaluation metrics
		mse = make_scorer(mean_squared_error)
		## model storage
		s = {} ## trait name as key, model as value
		s_mean = {} ## model name as key, mean as value
		#########################################
		## Lasso regression
		clf = linear_model.Lasso(alpha = 0.2)
		clf.fit(sample, label)
		score2 = cross_val_score(clf, sample, label, cv = 5, scoring = mse)
		print("Lasso Regression MSE: %0.2f (+/- %0.2f)" % (score2.mean(), score2.std() * 2))
		s["lasso"] = pickle.dumps(clf)
		s_mean["lasso"] = score2.mean()
		#########################################
		## Random Forest regressor
		clf = RandomForestRegressor(n_estimators = 20, n_jobs = -1)
		clf.fit(sample, label)
		score2 = cross_val_score(clf, sample, label, cv = 5, scoring = mse)
		print("Random Forest Regression MSE: %0.2f (+/- %0.2f)" % (score2.mean(), score2.std() * 2))
		s["sgd"] = pickle.dumps(clf)
		s_mean["sgd"] = score2.mean()
		#########################################
		## KNN regression
		clf = KNeighborsRegressor(weights = "distance", algorithm = "auto", n_jobs = -1)
		clf.fit(sample, label)
		score2 = cross_val_score(clf, sample, label, cv = 5, scoring = mse)
		print("KNN Regression MSE: %0.2f (+/- %0.2f)" % (score2.mean(), score2.std() * 2))
		s["knn"] = pickle.dumps(clf)
		s_mean["knn"] = score2.mean()
		#########################################
		## MLP regression
		clf = MLPRegressor(hidden_layer_sizes = (500,), learning_rate = "invscaling", max_iter = 1000)
		clf.fit(sample, label)
		score2 = cross_val_score(clf, sample, label, cv = 5, scoring = mse)
		print("MLP Regression MSE: %0.2f (+/- %0.2f)" % (score2.mean(), score2.std() * 2))
		s["gb"] = pickle.dumps(clf)
		s_mean["gb"] = score2.mean()
		#########################################
		## SGD regressor
		clf = linear_model.SGDRegressor(loss = "epsilon_insensitive", penalty = "l2")
		clf.fit(sample, label)
		score2 = cross_val_score(clf, sample, label, cv = 5, scoring = mse)
		print("SGD Regression MSE: %0.2f (+/- %0.2f)" % (score2.mean(), score2.std() * 2))
		s["sgd"] = pickle.dumps(clf)
		s_mean["sgd"] = score2.mean()
		#########################################
		## Gradient Boosting regression
		clf = GradientBoostingRegressor(loss = "huber", n_estimators = 100)
		clf.fit(sample, label)
		score2 = cross_val_score(clf, sample, label, cv = 5, scoring = mse)
		print("Gradient Boosting Regression MSE: %0.2f (+/- %0.2f)" % (score2.mean(), score2.std() * 2))
		s["gb"] = pickle.dumps(clf)
		s_mean["gb"] = score2.mean()
		## find the lowest mse
		h = min(s_mean, key = s_mean.get)
		print "\n"
		return pickle.loads(s[h])
	## save the best-fitting model for regression model
	## output: update model storage
	def saveModel(self):
		for item in self.name:
			print "processing regression model on trait: ", item
			print "classified as yes"
			self.modelYes[item] = pickle.dumps(self.trainModelRegression(item, "y"))
			print "classified as no"
			self.modelNo[item] = pickle.dumps(self.trainModelRegression(item, "n"))