## load packages
import re
from bs4 import BeautifulSoup as bs 
import urllib2
import csv

## data inilization
text = []

## functions
def readHTML(user):	
	my_page = urllib2.urlopen('https://twitter.com/' + str(user))
	soup = bs(my_page, 'lxml')
	return(soup)

def getText(soup):
	for item in soup.findAll('p', attrs = {'class': 'TweetTextSize TweetTextSize--normal js-tweet-text tweet-text'}):
		text.append(item.text.encode('utf-8'))


soup = readHTML("MayoClinic")
getText(soup)
for item in text:
	print item