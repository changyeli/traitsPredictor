## import packages
import os
import re
import csv
import string
from operator import add ## for list-wise element addition
import nltk
from nltk.corpus import stopwords

class fileProcess:
	def __init__(self):
		self.root = "/Users/changye.li/Documents/scripts/traitsPredictor/data/"
		self.feature = {} ## word feature
		self.totalChar = {} ## total words from user's tweet, with username as key
		self.document = [] ## documents ending with .txt, starting with tweet_
		self.userDocument = {} ## user tweet, with username as key, tweets as value
		self.tweetAttribute = {} ## user tweet attribute
	##better feature vector rewrite
	# update self.feature
	def formatFeature(self):
		word = set()
		category = set()
		temp = []
		## read feature file
		with open(self.root + "NRC.txt", "r") as f:
			for row in f:
				word.add(row.split()[0])
				category.add(row.split()[1])
				temp.append(row.split())
		category = list(category)
		## iterate word in feature file
		for item in word:
			## attributes
			attr = [0]*10
			## iterate each row in feature file
			for elem in temp:
				if elem[0] == item:
					if elem[1] in category:
						attr[category.index(elem[1])] = int(elem[2])
			## form a dictionary
			self.feature[item] = attr
		## write to file with better format
		with open("/Users/changye.li/Documents/scripts/traitsPredictor/data/better.csv", "wb") as f:
			writer = csv.writer(f)
			for key, value in self.feature.items():
				writer.writerow([key, value])
	## get all tweet_xxx.txt files
	# output: update self.document
	def getFiles(self):
		for r, d, f in os.walk(self.root):
			for files in f:
				if files.endswith(".txt") and files.startswith("tweet_"):
					self.document.append(files)
	## read files and write all users' tweets into a list, with username as key for a dict
	# input: filename to scan
	# output: update self.userDocument
	# output: update self.totalChar
	def readFiles(self, filename):
		## extract username
		s = filename[6:]
		s = s[:-4]
		## list to store all tweets 
		tweet = []
		with open(self.root+filename, "r") as f:
			for row in f:
				# remove RT, @ and url
				row = re.sub(r"(?:@\S*|#\S*|http(?=.*://)\S*)", "", row.rsplit("\n")[0].lower())
				row = row.replace("rt", "")
				tweet.append(row.rsplit("\n")[0].lower())
				tokens = []
				## tokenize all tweets
				for each in tweet:
					## remove all punctuations in a tweet
					temp = each.translate(None, string.punctuation)
					tokens.extend(nltk.word_tokenize(temp))
				## remove empty strings
				tokens = filter(None, tokens)
				x = [item for item in tokens if not item.startswith("http")]
				x = [re.sub(r'[^\w\s]', '', item) for item in tokens]
				## remove stopwords
				stop = set(stopwords.words("english"))
				x = [w for w in x if not w in stop]
				self.totalChar[s] = x
		self.userDocument[s] = tweet

