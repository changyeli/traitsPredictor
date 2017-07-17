## import ppackages
import nltk
from collections import Counter
import os

## find all .txt files
def getFiles():
	docs  = []
	for r, d, f in os.walk("/Users/changye.li/Documents/scripts/traitsPredictor"):
		for files in f:
			if files.endswith(".txt"):
				docs.append(files)
	return docs

## read file
# input: file name ends with .txt
# output: list that contains tweets for this user
def readFile(fileName):
	tweets = []
	with open(fileName, 'r') as f:
		for row in f:
			tweets.append(row.rsplit("\n")[0].lower())
	return tweets

## get training dataset for each account
# input: level of training dataset, eg: 0.7 of entire tweets
# output: dict, with username as key, tweets as values
def getTrain(level):
	docs = getFiles()
	train = {}
	for row in docs:
		tweets = readFile(row)
		size = int(len(tweets) * level)
		train_set = tweets[:size]
		## extract username
		row = row[-6:]
		row = row[:-4]
		train[row] = train_set
	return train

