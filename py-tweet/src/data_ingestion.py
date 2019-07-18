from os.path import dirname, realpath, join
import json
import pandas
from util.log import info, error
__author__  = 'Anthony Vilarim Caliani'
__contact__ = 'https://github.com/avcaliani'
__license__ = 'MIT'


# CONSTANTS
DATA_PATH = join(dirname(realpath(__file__)),'../data/tweets.txt')


def parse_tweets(file_path):
  data, file_content = [], open(file_path, 'r')
  for line in file_content:
    try:
      data.append(json.loads(line))
    except:
      error(f'Error while parsing data to JSON. Data: { line }')
  
  return data


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

  tweets_by_lang = tweets['lang'].value_counts()
  info(f'TOP 5 LANGUAGES IN WHICH THE TWEETS WERE WRITTEN\n{tweets_by_lang[:5]}')
  
  tweets_by_country = tweets['country'].value_counts()
  info(f'TOP 5 COUNTRIES FROM WHICH THE TWEETS WERE SENT\n{tweets_by_country[:5]}')
  
except (KeyboardInterrupt, SystemExit):
  info('Bye bye!', True)