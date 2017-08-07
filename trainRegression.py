## import packages
import os
import pandas as pd 
import nltk
import string
import sklearn
import numpy as np 
class trainRegression:
	def __init__(self):
		## path of vocabulary list in better format
		self.path = "/Users/changye.li/Documents/scripts/traitsPredictor/process/better.csv"
		## train dataset path
		self.files = "/Users/changye.li/Documents/scripts/traitsPredictor/mypersonality_final.csv"
		## data frame that contains all processed status
		## each entry represents word count of each user
		self.processed = pd.DataFrame()
		## vocabulary list in better format, with attributes
		self.better = pd.DataFrame()
		## vocabulary list
		self.voca = []
	def readFiles(self):
		self.better = pd.read_csv(self.path, names = ['voculabury', 'anticipation', 'joy', 'negative', 'sadness', 'disgust', 'positive', 'anger', 'surprise', 'fear', 'trust'])
		self.voca = self.better["voculabury"].values.tolist()
		