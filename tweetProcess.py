## import packages
import os
import re
import csv
import string
from operator import add ## for list-wise element addition
import nltk
from nltk.corpus import stopwords

class tweetProcess:
	def __init__(self):
		self.root = "/Users/changye.li/Documents/scripts/traitsPredictor/data/"
		self.process = "/Users/changye.li/Documents/scripts/traitsPredictor/process/"
		self.document = [] ## documents ending with .txt, starting with tweet_
	## get all tweet_xxx.txt files
	# output: update self.document
	def getFiles(self):
		for r, d, f in os.walk(self.root):
			for files in f:
				if files.endswith(".txt") and files.startswith("tweet_"):
					self.document.append(files)
		return self.document
	## read files and write all users' tweets into a list, with username as key for a dict
	# input: filename to scan
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
				## only keep letters in tokens
				x = [re.sub('[^a-zA-Z]+', '', w) for w in x]
				## write to file
				process_name = s + ".txt"
				with open(self.process+process_name, "w") as f:
					for each in x:
						f.write(each + ",")
			print "Finish " + s + "'s tweet process"
x = tweetProcess()
docs = x.getFiles()
for files in docs:
	x.readFiles(files)
