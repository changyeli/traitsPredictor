import csv
l1 = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
print [x + y for x, y in zip(l1, l1)]

with open(self.root +self.better, "w") as f:
			writer = csv.writer(f)
			for k, v in self.feature.iteritems():
				writer.writerow([k] + v)
with open('dict.csv', 'rb') as csv_file:
    reader = csv.reader(csv_file)
    mydict = dict(reader)


#def trainModel(self, df, filename):
		print "Process file: ", filename
		## add label column
		label = pd.read_csv(self.root + filename, usecols = [1])
		print df
		print label
		####################################
		# KNN
		clf3 = linear_model.SGDClassifier(loss = "log", penalty = "elasticnet")
		scores = cross_val_score(clf3, df, label, cv = 10, scoring = "f1")
		print("SGD Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
		####################################
		# MLP
		clf = MLPClassifier(solver = "adam", 
			alpha = 0.001, max_iter = 90000, hidden_layer_sizes = (1500, 10))
		scores = cross_val_score(clf, df, label, cv = 10, scoring = "f1")
		print("MLP Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
		#######################################
		# tree
		clf1 = tree.DecisionTreeClassifier(criterion = "entropy", splitter = "random", max_features = "sqrt")
		scores = cross_val_score(clf1, df, label, cv = 10, scoring = "f1")
		print("Dscision Tree Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
		###########################################
		# Bernoulli naive bayes
		clf2 = BernoulliNB()
		scores = cross_val_score(clf2, df, label, cv = 10, scoring = "f1")
		print("NB Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
