## import ppackages
import os
import re
import csv
from operator import add
import nltk
## find all .txt files
def getFiles():
	docs  = []
	for r, d, f in os.walk("/Users/changye.li/Documents/scripts/traitsPredictor/data/"):
		for files in f:
			if files.endswith(".txt") and files.startswith("tweet"):
				docs.append(files)
	return docs

## read file
# input: file name ends with .txt
# output: list with all tweets from this user
def readFile(fileName):
	tweets = []
	path = "/Users/changye.li/Documents/scripts/traitsPredictor/data/"
	with open(path + fileName, 'r') as f:
		for row in f:
			## remove RT, @ and url
			row = re.sub(r"(?:@\S*|#\S*|http(?=.*://)\S*)", "", row.rsplit("\n")[0].lower())
			row = row.replace("rt", "")
			tweets.append(row)
	return tweets

## read better-structured feature file
def readFeature():
	feature = {}
	with open("/Users/changye.li/Documents/scripts/traitsPredictor/data/better.csv", "rb") as f:
		reader = csv.reader(f)
		feature = dict(reader)
	return feature
## get featured word list

## get feature couting on each tweet
# input: single user tweet
# input: better-format features, witout
# output: dict, which username as key, feature count as value
def getFeature(tweet, feature):
	chars = []
	## break all tweets into single word
	for each in tweet:
		chars.extend(nltk.word_tokenize(each))
		## remove words that not appear in feature
		chars = [w for w in chars if w in fea]

## test run
def run():
	docs = getFiles()
	words = {}
	feature = readFeature()
	for each in docs:
		words[each] = readFile(each)
	
run()

