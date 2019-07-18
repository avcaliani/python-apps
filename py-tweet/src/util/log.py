__author__  = 'Anthony Vilarim Caliani'
__contact__ = 'https://github.com/avcaliani'
__license__ = 'MIT'
# Some Colors
ERROR_TAG = f'\033[1;31;40mERROR\033[0m'
INFO_TAG = f'\033[1;32;40mINFO\033[0m'

def info(data, no_tag=False):
  if no_tag:
    print(data)
  else:
    print(f'{ INFO_TAG }  => { data }')

def error(data):
  print(f'{ ERROR_TAG } => { data }')