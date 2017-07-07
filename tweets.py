import tweepy

consumer_key = 'B0ObhZGHXZdvdeGdGJRzsUp6B'
consumer_secret = '20gvy4MDnDPFglqqWPoR7vFsfk5otB9lC6WzA0mBBdqHI9khwN'
access_key = '140343853-OlHFgmgNZJwDfi1gXHDLhR5zmdjFvC3MVIvsMrLJ'
access_secret = 'cJKQWdJGVsib56vkGL18hO20x4KX5U56TEuHrmtYIWTJA'
totalTweets = []

## get up to 3200 tweet blocks from an account 
## inspired by: https://gist.github.com/yanofsky/5436496
def getTweets(userName):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	temp = api.user_timeline(userName, count = 200)
	totalTweets.extend(temp)
	last = totalTweets[-1].id - 1
	while len(temp) > 0:
		temp = api.user_timeline(userName, count = 200, max_id = last)
		totalTweets.extend(temp)
		last = totalTweets[-1].id - 1

getTweets("MayoClinic")
## extract tweet from blocks
result = [tweet.text.encode('utf-8') for tweet in totalTweets]
## write to .txt file
with open('tweet_mayo.txt', 'w') as f:
	for s in result:
		f.write(s + '\n')