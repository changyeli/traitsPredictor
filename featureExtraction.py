## import packages
import os
import csv
from operator import add ## for list-wise element addition
import nltk
## class and functions
class featureExtraction:
	def __init__(self):
		self.feature = {} ## better format of feature vocabulary
		self.userFeature = {} ## user word feature
		self.root = "/Users/changye.li/Documents/scripts/traitsPredictor/process/"
		self.better = "better.csv" ## better format feature
		self.nrc = "/Users/changye.li/Documents/scripts/traitsPredictor/data/NRC.txt" ## feature vocabulary
	## feature vector with better format
	def getFeature(self):
		word = set()
		category = set()
		temp = []
		## read feature file
		with open(self.nrc, "r") as f:
			for row in f:
				word.add(row.split()[0])
				category.add(row.split()[1])
				temp.append(row.split())
		features = {}
		category = list(category)
		## iterate word in feature file
		for item in word:
			feature = [0]*10
			## iterate each row in feature file
			for elem in temp:
				if elem[0] == item:
					if elem[1] in category:
						feature[category.index(elem[1])] = int(elem[2])
			## form a dictionary
			features[item] = feature
		## write to file with better format
		with open(self.root + self.better, "wb") as f:
			writer = csv.writer(f)
			for key, value in features.items():
				writer.writerow([key, value])
	## read better format feature file
	def readFeature(self):
		with open(self.root + self.better, "rb") as f:
			reader = csv.reader(f)
			self.feature = dict(reader)
x = featureExtraction()
x.getFeature()
x.readFeature()
for k,v in x.feature.items():
	print k, v
