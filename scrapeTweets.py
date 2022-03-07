# Contributors: Kasey La

# To run this file, type the following into the Shell:
#   python3 scrapeTweets.py

# In order to use this script, you need to first install snscrape and the pandas packages. In your bash Shell (not the python interpreter), run:
#   pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git
#   pip install pandas


# Imports
import os
import pandas


# Query by text search
# Setting variables to be used to format the command below

tweet_count = 500
wordList = ["\U0001F62D", "\U0001F5FF", "\U0001F480"]
start_date = "2022-02-19"
end_date = "2022-02-19"

count = 0
for word in wordList:
  search_string = '\"' + word + '\"'
  os.system("snscrape --jsonl --max-results {} --since {} twitter-search '{} until:{}'> {}-firstscrape.json".format(tweet_count, start_date, search_string, end_date, count))

  tweets_dataframe = pandas.read_json('{}-firstscrape.json'.format(count), lines=True)

  if len(tweets_dataframe) == 0 :
    print("Tweet Count of ", search_string, " : 0")
  else:
    tweets_dataframe.to_csv('{}-firstscrape.csv'.format(count), sep=',', index=False, columns=['date', 'content', 'id', 'url'])
  print("Tweet Count of ", search_string, " : ", str(len(tweets_dataframe)))
  count = count + 1