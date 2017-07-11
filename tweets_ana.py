## load package
import nltk
import re
from string import punctuation
from nltk import word_tokenize

## remove all punctuation
def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

## remove all emoticons
emoji_pattern = re.compile(
    u"(\ud83d[\ude00-\ude4f])|"  # emoticons
    u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
    u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
    u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
    u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
    "+", flags=re.UNICODE)
## tweet processing
# stupid version, need to be changed
def process(fileName):
	words = []
	with open(fileName, 'r') as f:
		words.extend(strip_punctuation(emoji_pattern.sub('', line)).rstrip() for line in f)
	token = [nltk.word_tokenize(i) for i in words]
	stop_words = nltk.corpus.stopwords.words('english')
	content = [w for w in token if w.lower() not in stop_words]
	return content
content = process('tweet_jimmyfallon.txt')
