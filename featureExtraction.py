## import packages
import os
import csv
from operator import add ## for list-wise element addition
import nltk
## class and functions
class featureExtraction:
	def __init__(self):
		self.feature = {} ## better format of feature vocabulary
		self.userFeature = {} ## user word feature, with word as key, attributes as value
		self.attr = [] ## the word list from feature, with order
		self.root = "/Users/changye.li/Documents/scripts/traitsPredictor/process/"
		self.better = "better.csv" ## better format feature
		self.nrc = "/Users/changye.li/Documents/scripts/traitsPredictor/data/NRC.txt" ## feature vocabulary file
		self.docs = [] ## document filenames for character-seperate file
		self.words = set() ## feature vocabulary
		self.allDocs = {} ## 
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
		features = {}
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
		
	## read character files
	def readFiles(self):
		for r, d, f in os.walk(self.root):
			for files in f:
				if files.endswith(".txt"):
					self.docs.append(files)
	## extract user feature based on better-formatted feature vocabulary
	def extractFeature(self):
		for each in self.docs:
			with open(self.root + each, "r") as f:
				s = each[:-4]
				## all words
				row = f.readline().split(",")
				## update user feature
				## only keep words that appear in feature vocabulary
				for item in row:
					if item in self.feature:
						if item in self.userFeature:
							self.userFeature[item].append(self.feature[item])
						else:
							self.userFeature[item] = [self.feature[item]]
				## integrate attributes
				for k, v in self.userFeature.iteritems():
					v = [sum(x) for x in zip(*v)]
					print v
				self.allDocs[s] = self.userFeature
## main function
x = featureExtraction()
x.readFiles()
x.getFeature()
x.extractFeature()
