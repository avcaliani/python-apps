# Some Colors
ERROR_TAG = f'\033[1;31;40mERROR\033[0m'
INFO_TAG = f'\033[1;32;40mINFO\033[0m'

def info(data):
  print(f'{ INFO_TAG }  => { data }')

def error(data):
  print(f'{ ERROR_TAG } => { data }')