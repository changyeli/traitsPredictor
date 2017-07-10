import tweepy
## auth info
consumer_key = 'B0ObhZGHXZdvdeGdGJRzsUp6B'
consumer_secret = '20gvy4MDnDPFglqqWPoR7vFsfk5otB9lC6WzA0mBBdqHI9khwN'
access_key = '140343853-OlHFgmgNZJwDfi1gXHDLhR5zmdjFvC3MVIvsMrLJ'
access_secret = 'cJKQWdJGVsib56vkGL18hO20x4KX5U56TEuHrmtYIWTJA'
## users and companies to scrape
com_tweet = ["Padilla_Comm", "MayoClinic", "Twitter", "TheEconomist", "Google", "nytimes"]
user_tweet = ["katyperry", "justinbieber", "BarackObama", "jimmyfallon", "EmmaWatson", "LeoDiCaprio", "HillaryClinton"]

## get up to 3200 tweet blocks from an account 
## inspired by: https://gist.github.com/yanofsky/5436496
def getTweets(userName):
	totalTweets = []
	try:
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_key, access_secret)
		api = tweepy.API(auth)
	except:
		print("Error: Authentication failed")
	temp = api.user_timeline(userName, count = 200)
	totalTweets.extend(temp)
	last = totalTweets[-1].id - 1
	while len(temp) > 0:
		temp = api.user_timeline(userName, count = 200, max_id = last)
		totalTweets.extend(temp)
		last = totalTweets[-1].id - 1
	return totalTweets

## file processing
def getTxt(screen):
	result = []
	s = "tweet_" + screen + '.txt'
	getTweets(screen)
	result = [tweet.text.encode('utf-8') for tweet in totalTweets]
	with open(s, 'w') as f:
		for item in result:
			f.write(item + '\n')

## get company tweets
for com in com_tweet:
	totalTweets = getTweets(com)
	getTxt(com)
## get user tweets
for user in user_tweet:
	totalTweets = getTweets(user)
	getTxt(user)
