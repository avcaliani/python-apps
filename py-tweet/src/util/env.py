import os

def get(key):
  value = os.getenv(key)
  print(f'{key}: {value}')
  return value