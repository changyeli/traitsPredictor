## load packages
import nltk
import os
import string
import re
from collections import Counter

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
## get list for all users' tweet
# input: list tweets; each entry is a tweet that user sent
# output: list that contains all words/tokenizers of users' tweet
def getDict(tweet):
	tokens = []
	## remove emoji
	emoji_pattern = re.compile(
    u"(\ud83d[\ude00-\ude4f])|"  # emoticons
    u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
    u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
    u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
    u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
    "+", flags=re.UNICODE)
	for each in tweet:
		## remove all punctuations in a tweet
		s = each.translate(None, string.punctuation)
		tokens.extend(nltk.word_tokenize(emoji_pattern.sub(r'', s)))

	return tokens

def run():
	docs = getFiles()
	tweets = []
	for each in docs:
		tweets.extend(readFile(each))
	tokens = getDict(tweets)
	## delete infrequent words
	c = Counter(x for x in tokens)
	c = c.items()
	delete_words = [x[0] for x in c if x[1] < 5]
	x = [item for item in tokens if item not in delete_words]
	x = list(set(x))
	x = x.sort()
	with open("documents.class", "w") as f:
		for each in x:
			f.write(each + ",")
run()
