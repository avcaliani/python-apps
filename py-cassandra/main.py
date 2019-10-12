import pandas as pd
from cassandra.cluster import Cluster

__author__ = 'Anthony Vilarim Caliani'
__contact__ = 'https://github.com/avcaliani'
__license__ = 'MIT'


def new_post(ss, row):
    ss.execute("""
    INSERT INTO posts (
        id, authors, date, analyzed, category, content, img_src, section, tags, title, topics, url
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        str(row.id), str(row.authors), str(row.date), bool(row.analyzed), str(row.category), str(row.content),
        str(row.img_src), str(row.section), str(row.tags), str(row.title), str(row.topics), str(row.url)
    ))


def new_author():
    # TODO: Do it
    pass


def update_author():
    # TODO: Do it
    pass


if __name__ == '__main__':

    print(f'Connecting to Cassandra cluster...')
    cluster = Cluster(['0.0.0.0'], port=9042)
    session = cluster.connect('py_cassandra_ks', wait_for_all_pools=True)

    # If you want to change the keyspace (It's not our case here)
    # session.set_keyspace('py_data')

    print(f'Reading data...')
    posts = pd.read_csv('data/techcrunch-posts.csv')
    posts['analyzed'] = False
    print(f'"{posts.shape[0]}" posts found!')

    print(f'Saving data to Cassandra database...')
    for i, post in posts.iterrows():
        new_post(session, post)

    print(f'"{session.execute("SELECT COUNT(*) FROM posts").one()[0]}" posts saved!')
    cluster.shutdown()
