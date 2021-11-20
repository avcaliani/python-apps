from datetime import datetime
from os import makedirs
from typing import Optional

from googleapiclient.discovery import build, Resource
from oauth2client.service_account import ServiceAccountCredentials
from pandas import DataFrame
from config import settings

# Google
SCOPES = settings.GOOGLE_API_SCOPES
SPREADSHEET_ID = settings.SPREADSHEET_ID
SPREADSHEET_RANGE = settings.SPREADSHEET_RANGE

# Data
OUTPUT_PATH = settings.OUTPUT_PATH


def auth(credentials_file: str) -> Resource:
    google_api = build(
        serviceName='sheets',
        version='v4',
        credentials=ServiceAccountCredentials.from_json_keyfile_name(credentials_file, SCOPES)
    )
    return google_api.spreadsheets()


def read(service: Resource) -> Optional[DataFrame]:
    result = service.values() \
        .get(spreadsheetId=SPREADSHEET_ID, range=SPREADSHEET_RANGE) \
        .execute() \
        .get('values', [])

    if not result:
        print('Data not found!')
        return None

    return DataFrame(result[1:], columns=result[0])


def write(df: DataFrame) -> None:
    makedirs(OUTPUT_PATH, exist_ok=True)
    now = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    df.to_csv(f'{OUTPUT_PATH}/new-users_{now}.csv', index=False)


def main():
    print('Authenticating at Google...')
    service = auth('credentials.json')

    print('Reading Google Sheets...')
    df = read(service)
    df.info(verbose=True)
    print(df)

    print('Writing data...', end=' ')
    write(df)
    print('Done \\o/')


if __name__ == '__main__':
    main()
