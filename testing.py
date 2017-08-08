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


## train models, file by file
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
		####################################
		# MLP
		clf = MLPClassifier(activation = "logistic", solver = "adam", 
			alpha = 0.001, max_iter = 900000, hidden_layer_sizes = (150000, ))
		clf.fit(train, labelTrain)
		labelPredict = clf.predict(test)
		## find the correct predictions
		rate = [i for i, j in zip(labelPredict, labelTest) if i == j]
		print "MLP correct rate: ", float(len(rate))/float(len(labelPredict))

		#######################################
		# SVM
		clf1 = svm.NuSVC(kernel = "sigmoid", nu = 0.3)
		clf1.fit(train, labelTrain)
		labelPredict1 = clf1.predict(test)
		rate1 = [i for i, j in zip(labelPredict1, labelTest) if i == j]
		print "SVM correct rate: ", float(len(rate1))/float(len(labelPredict1))
		
		###########################################
		# Bernoulli naive bayes
		clf2 = BernoulliNB()
		clf2.fit(train, labelTrain)
		labelPredict2 = clf2.predict(test)
		rate2 = [i for i, j in zip(labelPredict2, labelTest) if i == j]
		print "Bernoulli Naive Bayes correct rate: ", float(len(rate2))/float(len(labelPredict2))
		
		###########################################
		# KNN
		clf3 = KNeighborsClassifier(n_neighbors = 10, weights = "distance")
		clf3.fit(train, labelTrain)
		labelPredict3 = clf3.predict(test)
		rate3 = [i for i, j in zip(labelPredict3, labelTest) if i == j]
		print "KNN correct rate: ", float(len(rate3))/float(len(labelPredict3))