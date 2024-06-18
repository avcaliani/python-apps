from argparse import ArgumentParser

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import INTEGER, TEXT, DATE

from src.util import Timer

DB_NAME = 'postgres-app'
DB_SCHEMA = 'development'
TABLE_NAME = 'user_score'
TABLE_DTYPE = {
    'name': TEXT,
    'email': TEXT,
    'document': TEXT,
    'score': INTEGER,
    'updated_at': DATE,
}


def get_args():
    parser = ArgumentParser(description='Postgres App')
    parser.add_argument('pipeline', help='Pipeline')
    return parser.parse_args()


def read_file(file_path):
    print('=~=~=~=~=~=~=~= READ =~=~=~=~=~=~=~=')
    print(f'File: {file_path}')
    df = pd.read_csv(file_path)
    print(f'Lines: {df.shape[0]}')
    print(f'Columns: {df.shape[1]}')
    df.info(verbose=True)
    return df


def credentials():
    db_user = 'app-user'
    db_password = 'pass4app'
    db_host = 'localhost'
    return f'postgresql://{db_user}:{db_password}@{db_host}/{DB_NAME}'


def report():
    print('=~=~=~=~=~=~= READ SQL =~=~=~=~=~=~=')
    db = create_engine(credentials()).connect()
    df = pd.read_sql(
        sql=f"""
        select 
            count(*) as records,
            count(distinct document) as users 
        from "{DB_NAME}"."{DB_SCHEMA}".user_score
        """,
        con=db
    )
    print(df)
    df = pd.read_sql(
        sql=f'select * from "{DB_NAME}"."{DB_SCHEMA}".user_score limit 10',
        con=db
    )
    df.info(verbose=True)
    print(df)


def save(conn, df, table, overwrite):
    wr_timer = Timer()
    print('=~=~=~=~=~=~=~= WRITE =~=~=~=~=~=~=~')
    print(f'Schema: {DB_SCHEMA}')
    print(f'Table: {table}')
    print(f'Overwrite: {overwrite}')
    df.to_sql(
        name=table,
        con=conn,
        if_exists='replace' if overwrite else 'append',
        index=False,
        schema=DB_SCHEMA,
        dtype=TABLE_DTYPE,
    )
    print(f'Elapsed time: {wr_timer.stop()}')


if __name__ == '__main__':
    args, timer = get_args(), Timer()
    print(f'Args: {args}')
    pipeline = str(args.pipeline).lower().strip()
    if pipeline == 'report':
        report()
    elif pipeline == 'save':
        db = create_engine(credentials()).connect()
        # Auto Generated Table
        save(conn=db, df=read_file('./data/user-score.csv'), table=TABLE_NAME, overwrite=True)
        # Existing Table
        save(conn=db, df=read_file('./data/user-score-history.csv'), table=f'{TABLE_NAME}_history', overwrite=False)
    else:
        raise RuntimeError(f'Pipeline "{args.pipeline}" does not exist.')
    print(f'App executed in {timer.stop()}')
