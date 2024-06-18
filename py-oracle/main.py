from os import environ
from cx_Oracle import connect, Error

HOST = environ.get('DB_HOST', 'localhost')
PORT = environ.get('DB_PORT', '1521')
SID = environ.get('DB_SID', 'xe')
USER = environ.get('DB_USER', 'system')
PASSWORD = environ.get('DB_PASSWORD', 'oracle')
SEPARATOR = '----------------------------------------'


def main():
    try:
        describe()
        with connect(USER, PASSWORD, f'{HOST}:{PORT}/{SID}', encoding='UTF-8') as conn:
            print(f'Oracle Version: {conn.version}')
            cursor = conn.cursor()
            show_users(cursor)
            cursor.close()
        print("That's all folks!")
    except (Error, Exception) as err:
        print(f'FATAL: {err}')


def describe():
    print(f'{SEPARATOR}\nDATABASE\n{SEPARATOR}')
    print(f'Host: {HOST}')
    print(f'Port: {PORT}')
    print(f'SID: {SID}')
    print(f'User: {USER}')
    print(f'Password: {PASSWORD}')


def show_users(cursor):
    cursor.execute('SELECT * FROM APP.DEVELOPERS')
    print(f'\n{SEPARATOR}\nDEVELOPERS\n{SEPARATOR}')
    for user in cursor:
        print(user)


if __name__ == '__main__':
    main()
