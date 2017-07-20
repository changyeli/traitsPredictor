## import ppackages
import os
import re
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
# output: dict, with usename as key, all tweets as values
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


## test run
def run():
	docs = getFiles()
	words = {}
	for each in docs:
		words[each] = readFile(each)
run()

