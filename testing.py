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
		df.columns = self.attr[1:]
		label = pd.read_csv(self.root + filename, usecols = [1])
		df = df.assign(label = label.values)
		####################################
		# KNN
		clf3 = linear_model.SGDClassifier(loss = "log", penalty = "elasticnet")
		predicted = cross_val_predict(clf3, df[self.attr[1:]], df["label"], cv = 10)
		print "SGD CV score: ", metrics.accuracy_score(df["label"], predicted, normalize = True)
		####################################
		# MLP
		clf = MLPClassifier(solver = "adam", 
			alpha = 0.001, max_iter = 90000, hidden_layer_sizes = (1500, 10))
		predicted = cross_val_predict(clf, df[self.attr[1:]], df["label"], cv = 10)
		print "MLP CV score: ", metrics.accuracy_score(df["label"], predicted, normalize = True)
		#######################################
		# tree
		clf1 = tree.DecisionTreeClassifier(criterion = "entropy", splitter = "random", max_features = "sqrt")
		redicted = cross_val_predict(clf1, df[self.attr[1:]], df["label"], cv = 10)
		print "Decision Tree CV score: ", metrics.accuracy_score(df["label"], predicted, normalize = True)
		###########################################
		# Bernoulli naive bayes
		clf2 = BernoulliNB()
		predicted = cross_val_predict(clf2, df[self.attr[1:]], df["label"], cv = 10)
		print "NB CV score: ", metrics.accuracy_score(df["label"], predicted, normalize = True)