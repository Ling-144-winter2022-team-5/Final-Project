import tweepy
import pandas

client = tweepy.Client(bearer_token='INSERT-BEARER-TOKEN')

# this function will search for tweets including the skull emoji
def skull_tweets():
  query = '\U0001F480'

  tweetList = []

  for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100).flatten(limit=1000):
    tweetList.append(tweet.text)

  tweetDataframe = pandas.DataFrame(tweetList)
  tweetDataframe.to_csv('skull.csv', header=['Tweets'], index=False)

  print('done with skull_tweets')

# this function will search for tweets including the crying emoji
def crying_tweets():
  query = '\U0001F62D'

  tweetList = []

  for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100).flatten(limit=1000):
    tweetList.append(tweet.text)

  tweetDataframe = pandas.DataFrame(tweetList)
  tweetDataframe.to_csv('crying.csv', header=['Tweets'], index=False)

  print('done with crying_tweets')

skull_tweets()
crying_tweets()