import csv
class featureExtraction:
	def __init__(self):
		self.feature = {} ## better format of feature vocabulary
		self.attr = [] ## the word category list from feature, with order
		self.root = "/Users/changye.li/Documents/scripts/traitsPredictor/process/"
		self.better = "better.csv" ## better format feature
		self.nrc = "/Users/changye.li/Documents/scripts/traitsPredictor/data/NRC.txt"
		self.words = set() ## feature vocabulary
	## feature vector with better format
	def getFeature(self):
		category = set()
		temp = []
		## read feature file
		with open(self.nrc, "r") as f:
			for row in f:
				self.words.add(row.split()[0])
				category.add(row.split()[1])
				temp.append(row.split())
		category = list(category)
		## iterate word in feature file
		for item in self.words:
			feature = [0]*10
			## iterate each row in feature file
			for elem in temp:
				if elem[0] == item:
					if elem[1] in category:
						feature[category.index(elem[1])] = int(elem[2])
			## form a dictionary
			self.feature[item] = feature
			self.attr = category
		with open(self.root +self.better, "w") as f:
			writer = csv.writer(f)
			for k, v in self.feature.iteritems():
				writer.writerow([k] + v)
x = featureExtraction()
x.getFeature()