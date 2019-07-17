import pandas
import requests as http
from bs4 import BeautifulSoup
from util.log import info, error
__author__  = 'Anthony Vilarim Caliani'
__contact__ = 'https://github.com/avcaliani'
__license__ = 'MIT'

# CONSTANTS
URL = 'https://www.basketball-reference.com/leagues/NBA_2018_totals.html'


def get_data():

  info(f'Requesting "{ URL }"')
  req = http.get(URL)

  info(f'Request Status: { req.status_code }')
  if req.status_code != 200:
    error(f'Fail to request source! Code { req.status_code }')
    return

  content = req.content
  soup = BeautifulSoup(content, 'html.parser')
  table = soup.find(name='table')

  # Data Frame
  df = pandas.read_html(str(table))[0]
  info(f'Data Frame created! ({ df.shape[0] } records)\n{ df }')
  return df


def run():

  # Getting Data
  df = get_data()

  # Data Cleanup
  df_size = df.shape[0]
  to_drop = df[ df['Rk'] == 'Rk' ].index
  df.drop(to_drop, inplace=True)
  info(f'{ to_drop.size } records has been dropped! Records remaining: { df.shape[0] } of { df_size }')

  # Formatting Data
  numeric_cols = df.columns.drop(['Player', 'Pos', 'Tm'])
  df[numeric_cols] = df[numeric_cols].apply(pandas.to_numeric)

  # Sorting Data
  sorted_df = df.sort_values(by=['3P'], axis=0, ascending=False)
  info(f'Sorted Data Frame!\n{ sorted_df[["Player", "3P"]].head() }')


run()
