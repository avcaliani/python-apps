from datetime import datetime
from cassandra.cluster import Cluster

__author__ = 'Anthony Vilarim Caliani'
__contact__ = 'https://github.com/avcaliani'
__license__ = 'MIT'


if __name__ == '__main__':

    print(f'Connecting to our cluster...')
    cluster = Cluster(['0.0.0.0'], port=9042)
    session = cluster.connect('py_data', wait_for_all_pools=True)

    # If you want to change the keyspace (It's not our case here)
    # session.set_keyspace('py_data')

    print(f'Posts: {session.execute("SELECT COUNT(*) FROM posts").one()[0]}')
    print(f'Inserting new post...')
    session.execute(
        "INSERT INTO posts (id, author, title, content, published_at) VALUES (%s, %s, %s, %s, %s)",
        (4, 'isa', 'Post 04', 'Content 04', datetime.utcnow())
    )

    print(f'(Updated) Posts: {session.execute("SELECT COUNT(*) FROM posts").one()[0]}')
    rows = session.execute('SELECT * FROM posts')
    for row in rows:
        print(row.id, row.author, row.title, row.content, row.published_at)
