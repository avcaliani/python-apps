__author__  = 'Anthony Vilarim Caliani'
__contact__ = 'https://github.com/avcaliani'
__license__ = 'MIT'


# CONSTANTS
DEBUG_TAG = f'\033[1;35;40mDEBUG\033[0m'
ERROR_TAG = f'\033[1;31;40mERROR\033[0m'
INFO_TAG = f'\033[1;32;40mINFO\033[0m'
DEBUG_ENABLED = True


def info(data, no_tag=False):
  if no_tag:
    print(data)
  else:
    print(f'{ INFO_TAG }  => { data }')


def error(data):
  print(f'{ ERROR_TAG } => { data }')


def debug(data):
  if DEBUG_ENABLED:
    print(f'{ DEBUG_TAG } => { data }')
