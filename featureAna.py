## import packages
import csv
import numpy as np 
import pandas as pd 
class featureAna:
	def __init__(self):
		self.root = "/Users/changye.li/Documents/scripts/traitsPredictor/clean/"
		self.fileName1 = "allData.csv"
		self.fileName2 = "labels.txt"
		self.allData = pd.DataFrame() ## read all data
		self.labels = [] ## read all labels
		self.attr = ['anticipation', 'joy', 'negative', 'sadness', 'disgust', 'positive', 'anger', 'surprise', 'fear', 'trust'] ## attribute vocabulary
	## read pre-processed files
	def readFiles(self):
		self.allData = pd.read_csv(self.root + self.fileName1)
		with open(self.root + self.fileName2, "r") as f:
			content = f.readlines()
		self.labels = [int(x.strip()) for x in content]
	def getCluster(self, seq, item):
		dup = []
		offset = -1
		while True:
			try:
				offet = seq.index(item, offset+1)
			except ValueError:
				return result
			dup.append(offset)
		return dup

## test
x = featureAna()
x.readFiles()
labels = x.labels
temp = x.getCluster(labels, 0)
print temp