## import package
import os
import numpy as np 
import csv
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

class featureBuild:
	def __init__(self):
		self.root = "/Users/changye.li/Documents/scripts/traitsPredictor/clean/"
		self.docs = [] ## file names under self.root
		self.allData = pd.DataFrame()
	def readFile(self):
		for r, d, f in os.walk(self.root):
			for files in f:
				if files.endswith(".csv"):
					self.docs.append(files)
	def scanData(self):
		for each in self.docs:
			path = self.root + each
			## read file to data frame
			df = pd.read_csv(path, delimiter = ",")
			## remove rows with all zeros
			df = df[(df.T != 0).any()]
			self.allData.append(df)
x = featureBuild()
x.readFile()
x.scanData()
print x.allData