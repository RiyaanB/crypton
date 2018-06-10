import datetime
import tweepy

"""" This module's primary purpose is to scrape tweets from the internet and allow us to rate the sentiment within it"""

consumer_key = 'eofvfSE2IueXsMlbEAuylAxNL'
consumer_secret = 'Griv6wHexwCfGwWpifGacZfd4etoG3EVMCC10qFnLpVFUOeJmG'

access_token = '140024424-UrjXzn1nIkE7CkjXZGb37XxI6JAuRwve1awBqj1Q'
access_token_secret = 'bdKQwQB6OGPSGlvD9L3jKul68X8Xgvi4uY1XaqTreQPW3'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

l = [
    open('./Tweets/dn', 'a'),
    open('./Tweets/mn', 'a'),
    open('./Tweets/mp', 'a'),
    open('./Tweets/dp', 'a'),
]

startUNIXTime = 1527638400

for tweet in tweepy.Cursor(api.search, q="Bitcoin -BTC -cash min_retweets:100", lang="en", rpp=200,).items():
    print("Text: " + tweet.text)
    print("Date: " + str(tweet.created_at))
    print("Followers: " + str(tweet.user.followers_count))
    print("Retweets:  " + str(tweet.retweet_count))

    group = int(input("Choice: "))
    if group < 0 or group >= 4:
        continue
    else:
        l[group].write(str((tweet.created_at.timestamp() - startUNIXTime)/3600) + "\n")
        l[group].flush()
