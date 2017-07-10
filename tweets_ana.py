## load package
import textblob
import nltk
import re
from string import punctuation

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
## read file
### every tweet 
words = []
with open('tweet_jimmyfallon.txt', 'r') as f:
	words.extend(strip_punctuation(emoji_pattern.sub('', line)).split() for line in f)

print words