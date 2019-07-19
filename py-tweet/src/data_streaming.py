from os.path import dirname, realpath, join
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
import util.env as env
from util.log import info, error
__author__  = 'Anthony Vilarim Caliani'
__contact__ = 'https://github.com/avcaliani'
__license__ = 'MIT'


# CONSTANTS
CONSUMER_KEY = env.get('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = env.get('TWITTER_CONSUMER_SECRET')
ACCESS_TOKEN = env.get('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = env.get('TWITTER_ACCESS_TOKEN_SECRET')
OUTPUT_FILE = join(dirname(realpath(__file__)),'../data/tweets.txt')


class TweetListener(StreamListener):

  def __init__(self, file_name):
    self.file = open(file_name, 'a+')

  def on_data(self, data):
    info(data)
    self.file.write(data)
    return True

  def on_error(self, status):
    error(status)

  def __del__(self):
    self.file.close()


info("""
   ____           _____                        _   
  |  _ \  _   _  |_   _|__      __  ___   ___ | |_ 
  | |_) || | | |   | |  \ \ /\ / / / _ \ / _ \| __|
  |  __/ | |_| |   | |   \ V  V / |  __/|  __/| |_ 
  |_|     \__, |   |_|    \_/\_/   \___| \___| \__|
          |___/                       by @avcaliani


TWEETS STREAMING 🐦
Press Ctrl+c to stop
""", True)

stream = None
try:

  auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

  stream = Stream(auth, TweetListener(OUTPUT_FILE))
  stream.filter(track=['python', 'javascript', 'ruby'])
  
except (KeyboardInterrupt, SystemExit):
  if stream is not None:
    stream.disconnect()
  info('Bye bye!', True)