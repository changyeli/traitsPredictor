## import ppackages
import nltk
import os
import numpy
import sklearn
from sklearn.feature_extraction import DictVectorizer

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
# input: list of files to iterate
# output: dict, with username as key, tweets as values
def getTrain(level, docs):
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
## get test dataset for each account
# input: level of training dataset
# input: list of files to iterate
# output: dict, with username as key, tweets as values
def getTest(level, docs):
	test = {}
	for row in docs:
		tweets = readFile(row)
		size = int(len(tweets) * level)
		test_set = tweets[size:]
		row = row[-6:]
		row = row[:-4]
		test[row] = test_set
	return test
## tag all words in .class file
# input: .class file that contains all words
# output: a list contain pos of words
def getPOS(fileName):
	words = []
	with open(fileName, 'r') as f:
		for row in f:
			words.extend(row.split(","))
	## remove empty string
	words = filter(None, words)
	return nltk.pos_tag(words)

def run():
	docs = getFiles()
	train = getTrain(0.7, docs)
	test = getTest(0.7, doce)
	words = getPOS("documents.class")
