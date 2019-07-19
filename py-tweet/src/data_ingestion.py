from os.path import dirname, realpath, join
import re
import json
import pandas
from util.log import info, error, debug
__author__  = 'Anthony Vilarim Caliani'
__contact__ = 'https://github.com/avcaliani'
__license__ = 'MIT'


# CONSTANTS
DATA_PATH = join(dirname(realpath(__file__)),'../data/tweets.txt')
LINK_REGEX = r'https?://[^\s<>"]+|www\.[^\s<>"]+'


def parse_tweets(file_path):
  data, file_content = [], open(file_path, 'r')
  for line in file_content:
    try:
      data.append(json.loads(line))
    except:
      error(f'Error while parsing data to JSON. Data: { line }')
  
  return data


def word_in_text(word, text):
  _word, _text = str(word).lower(), str(text).lower()
  return True if re.search(_word, _text) else False


def extract_link(text):
  match = re.search(LINK_REGEX, str(text))
  return match.group() if match else ''


info("""
   _              _  _    _               
  | |_ __      __(_)| |_ | |_   ___  _ __ 
  | __|\ \ /\ / /| || __|| __| / _ \| '__|
  | |_  \ V  V / | || |_ | |_ |  __/| |   
   \__|  \_/\_/  |_| \__| \__| \___||_|   


TWEETS INGESTION 🤘
Press Ctrl+c to stop
""", True)

try:

  file_content = parse_tweets(DATA_PATH)
  info(f'{ len(file_content) } tweets found!')

  tweets = pandas.DataFrame()
  tweets['text'] = list(map(lambda d: d['text'], file_content))
  tweets['lang'] = list(map(lambda d: d['lang'], file_content))
  tweets['country'] = list(map(
    lambda d: d['place']['country'] if d['place'] != None else None,
    file_content
  ))

  # Looking for tweets origin
  tweets_by_lang = tweets['lang'].value_counts()
  tweets_by_country = tweets['country'].value_counts()

  debug(tweets)
  debug(f'"tweets" Data Frame Shape: { tweets.shape }')

  info("=~= TOP 5 =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=")
  info(f'Languages In Which The Tweets Were Written\n{ tweets_by_lang[:5] }')
  info(f'Countries From Which The Tweets Were Sent\n{ tweets_by_country[:5] }')
  info(f'Available Tweets: { tweets.shape[0] }\n')


  # Searching Python, Ruby, and Javascript related tweets
  tweets['python'] = tweets['text'].apply(lambda tweet: word_in_text('python', tweet))
  tweets['javascript'] = tweets['text'].apply(lambda tweet: word_in_text('javascript', tweet))
  tweets['ruby'] = tweets['text'].apply(lambda tweet: word_in_text('ruby', tweet))

  debug(tweets)
  debug(f'"tweets" Data Frame Shape: { tweets.shape }')

  info("=~= REFERENCES  =~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=")
  info(f'* Python            { tweets["python"].value_counts()[True] }')
  info(f'* JS                { tweets["javascript"].value_counts()[True] }')
  info(f'* Ruby              { tweets["ruby"].value_counts()[True] }')
  info(f'* Available Tweets  { tweets.shape[0] }\n')


  # Searching relevant tweets
  tweets['programming'] = tweets['text'].apply(lambda tweet: word_in_text('programming', tweet))
  tweets['tutorial'] = tweets['text'].apply(lambda tweet: word_in_text('tutorial', tweet))
  tweets['relevant'] = tweets['text'].apply(lambda tweet: word_in_text('programming', tweet) or word_in_text('tutorial', tweet))
  relevant_tweets = tweets[tweets['relevant'] == True]

  debug(tweets)
  debug(f'"tweets" Data Frame Shape: { tweets.shape }')

  info("=~= RELEVANT TWEETS =~=~=~=~=~=~=~=~=~=~=~=~=~=")
  info(f'* Tweets about "programming"      { tweets["programming"].value_counts()[True] }')
  info(f'* Tweets about "tutorial"         { tweets["tutorial"].value_counts()[True] }')
  info(f'* --')
  info(f'* Relevant Tweets                 { tweets["relevant"].value_counts()[True] }')
  info(f'* Relevant Tweets about "Python"  { relevant_tweets["python"].value_counts()[True] }')
  info(f'* Relevant Tweets about "JS"      { relevant_tweets["javascript"].value_counts()[True] }')
  info(f'* Relevant Tweets about "Ruby"    { relevant_tweets["ruby"].value_counts()[True] }')
  info(f'* Available Tweets                { tweets.shape[0] }\n')


  # Searching relevant tweets with links
  tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))
  relevant_tweets = tweets[tweets['relevant'] == True]
  tweets_with_links = relevant_tweets[relevant_tweets['link'] != '']

  debug(tweets)
  debug(f'"tweets" Data Frame Shape: { tweets.shape }')

  info("=~= RELEVANT TWEETS WITH LINK =~=~=~=~=~=~=~=~=")
  info(f'* Relevant Tweets                 { relevant_tweets.shape[0] }')
  info(f'* Relevant Tweets with Link       { tweets_with_links.shape[0] }')
  info(f'* Relevant Tweets about "Python"  { tweets_with_links[ tweets_with_links["python"] == True ].shape[0] }')
  info(f'* Relevant Tweets about "JS"      { tweets_with_links[ tweets_with_links["javascript"] == True ].shape[0] }')
  info(f'* Relevant Tweets about "Ruby"    { tweets_with_links[ tweets_with_links["ruby"] == True ].shape[0] }')
  info(f'* Available Tweets                { tweets.shape[0] }\n')


except (KeyboardInterrupt, SystemExit):
  info('Bye bye!', True)