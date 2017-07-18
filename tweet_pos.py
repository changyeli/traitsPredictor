## import ppackages
import os
import re
## find all .txt files
def getFiles():
	docs  = []
	for r, d, f in os.walk("/Users/changye.li/Documents/scripts/traitsPredictor/data"):
		for files in f:
			if files.endswith(".txt") and files.startswith("tweet"):
				docs.append(files)
	return docs

## read file
# input: file name ends with .txt
# output: list that contains tweets for this user
def readFile(fileName):
	tweets = []
	with open(fileName, 'r') as f:
		for row in f:
			## remove RT, @ and url
			row = re.sub(r"(?:@\S*|#\S*|http(?=.*://)\S*)", "", row.rsplit("\n")[0].lower())
			row = row.replace("rt", "")
			tweets.append(row)
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
		test[row] = test_set
	return test
def readNRC():


## test run
def run():
	docs = getFiles()
	train = getTrain(0.7, docs)
	test = getTest(0.7, docs)
run()
