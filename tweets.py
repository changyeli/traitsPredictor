import tweepy

consumer_key = "B0ObhZGHXZdvdeGdGJRzsUp6B"
consumer_secret = "20gvy4MDnDPFglqqWPoR7vFsfk5otB9lC6WzA0mBBdqHI9khwN"
access_key = "140343853-OlHFgmgNZJwDfi1gXHDLhR5zmdjFvC3MVIvsMrLJ"
access_secret = "cJKQWdJGVsib56vkGL18hO20x4KX5U56TEuHrmtYIWTJA"

user = "Padilla_Comm"
auto = tweepy.OAuthHandler(consumer_key, consumer_secret)
auto.set_access_token(access_key, access_secret)
api = tweepy.API(auto)

client = api.get_user(user)
print(client.screen_name)