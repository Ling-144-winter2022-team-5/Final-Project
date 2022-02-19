# Dataset

This folder currently contains 5 files:

 1. this **README** file
 2. **tweepy-tweet-scraper.py**, a script that was used to scrape data from Twitter of the emojis 😭, 💀, and 🗿 from tweets posted on February 19, 2022.
 3. **crying.csv**, a file containing the tweets with the emoji 😭 that were scraped, gathered on February 19, 2022.
 4. **skull.csv**, a file containing the tweets with the emoji 💀 that were scraped, gathered on February 19, 2022.
 5. **moai.csv**, a file containing the tweets with the emoji 🗿 that were scraped, gathered on February 19, 2022.

In the future, these tweets will be filtered to primarily look at sentence final occurrences of these emojis. 
This is to ensure that we’re looking at the emojis in similar contexts. 
We chose sentence final occurrences because we feel like those are the instances when they’re most often used as ‘mood markers’. 
We will also be filtering to focus on primarily English tweets (we may look at Tweets in languages other than English, 
but these would need to be picked out and examined by hand). Once we have our list of filtered tweets, 
we will need to annotate them by what the conveyed mood is, and then compare that with the intended meaning and/or expected mood of each emoji.
