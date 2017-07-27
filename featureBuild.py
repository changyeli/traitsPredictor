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
		self.allData = pd.DataFrame() ## dataframe to store all matrices
		self.attr = ['anticipation', 'joy', 'negative', 'sadness', 'disgust', 'positive', 'anger', 'surprise', 'fear', 'trust']
	def readFile(self):
		for r, d, f in os.walk(self.root):
			for files in f:
				if files.endswith(".csv"):
					self.docs.append(files)
	## scan all matrices from self.docs
	def scanData(self):
		for each in self.docs:
			path = self.root + each
			## read file to data frame
			df = pd.read_csv(path, delimiter = ",", names = self.attr)
			## remove rows with all zeros
			df = df[(df.T != 0).any()]
			self.allData = self.allData.append(df)
	## create k-means for full matrix
	## ruduce dimension using PCA, and plot the result of k-means
	def fullKMeans(self):
		## reduce dimension using PCA
		reduced = PCA(n_components = 2).fit_transform(self.allData)
		## big-five style, using EM algorithm
		km = KMeans(n_clusters = 5, algorithm = "full", max_iter = 1000).fit(reduced)
		## step size of the mesh
		h = 0.2
		## boundary
		x_min, x_max = reduced[:, 0].min() - 1, reduced[:, 0].max() + 1
		y_min, y_max = reduced[:, 1].min() - 1, reduced[:, 1].max() + 1
		xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
		z = km.predict(np.c_[xx.ravel(), yy.ravel()])
		z = z.reshape(xx.shape)
		## plot the figure
		plt.figure(1)
		plt.clf()
		plt.imshow(z, interpolation = 'nearest', extent = (xx.min(), xx.max(), yy.min(), yy.max()), cmap = plt.cm.Paired, aspect = 'auto', origin = 'lower')
		plt.plot(reduced[:, 0], reduced[:, 1], "k.", markersize = 2)
		centroid = km.cluster_centers_
		plt.scatter(centroid[:, 0], centroid[:, 1], marker = 'x', s = 169, linewidths = 3, color = 'w', zorder = 10)
		plt.title('K-means clustering on the digits dataset (PCA-reduced data)\n'
		          'Centroids are marked with white cross')
		plt.xlim(x_min, x_max)
		plt.ylim(y_min, y_max)
		plt.xticks(())
		plt.yticks(())
		plt.show()
x = featureBuild()
x.readFile()
x.scanData()
x.fullKMeans()