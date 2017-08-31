import os
import re
import string
import pandas as pd
from nltk.corpus import stopwords
class tweetProcess:
	def __init__(self):
		self.root = "/Users/changye.li/Documents/scripts/traitsPredictor/data/"
		self.process = "/Users/changye.li/Documents/scripts/traitsPredictor/process/"
		self.stop = list(set(stopwords.words("english")))
		self.word = []
	## get all tweet_xxx.txt files
	# output: update self.document
	def getFiles(self):
		document = []
		for r, d, f in os.walk(self.root):
			for files in f:
				if files.endswith(".txt") and files.startswith("tweet_"):
					document.append(files)
		return document
	## get NRC word list and associated attributes
	def getValues(self):
		better = {}
		nrc = pd.read_csv(self.process + "better.csv", header = None, index_col = False)
		for index, row in nrc.iterrows():
			better[row[0]] = row[1:].values.tolist()
			self.word.append(row[0])
		return better
	## read files and write all users' tweets
	# input: filename to scan
	# input: NRC word attributes
	def readFiles(self, filename, values):
		with open(self.root+filename, "r") as f:
			tweet = [] ## attribute matrix for each user
			for row in f:
				attr = [] ## store attributes for each tweet
				# remove RT, @ and url
				row = re.sub(r"(?:@\S*|#\S*|http(?=.*://)\S*)", "", row.rsplit("\n")[0].lower())
				row = row.replace("rt", "").rsplit("\n")[0]
				for word in row.translate(None, string.punctuation).split():
					if(word in self.word and word not in self.stop):
						attr.append(values[word])
					else:
						continue
				tweet.append([sum(x) for x in zip(*attr)])
			tweet = filter(None, tweet)
			s = filename[6:]
			s = s[:-4]
			pd.DataFrame(tweet).to_csv(self.process + s + ".csv", header = False, index = False)
x = tweetProcess()
docs = x.getFiles()
better = x.getValues()
for item in docs:
	x.readFiles(item, better)