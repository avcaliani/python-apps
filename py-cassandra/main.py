import pandas as pd
import numpy as np
from cassandra.cluster import Cluster


def new_post(ss, row):
    ss.execute("""
    INSERT INTO posts (
        id, authors, date, analyzed, category, content, img_src, section, tags, title, topics, url
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        str(row.id), str(row.authors), str(row.date), bool(row.analyzed), str(row.category), str(row.content),
        str(row.img_src), str(row.section), str(row.tags), str(row.title), str(row.topics), str(row.url)
    ))


def new_author(ss, row):
    ss.execute(
        "INSERT INTO authors (author, verified_posts, not_verified_posts) VALUES (%s, %s, %s)",
        (str(row.authors), int(row.verified_posts), int(row.not_verified_posts))
    )


def calc_authors_data(df):
    _posts = df[['authors', 'analyzed']]

    # Calculating analyzed posts
    df_analyzed = _posts[_posts.analyzed == True].groupby('authors').count()
    df_analyzed.columns = ['verified_posts']

    # Calculating posts to be analyzed
    df_not_analyzed = _posts[_posts.analyzed == False].groupby('authors').count()
    df_not_analyzed.columns = ['not_verified_posts']

    authors = posts[['authors']].drop_duplicates(keep='first')
    merged_df = authors.merge(
        df_analyzed, how='left', on='authors'
    ).merge(
        df_not_analyzed, how='left', on='authors'
    )

    merged_df.fillna(0, inplace=True)
    merged_df["verified_posts"] = merged_df["verified_posts"].astype(int)
    merged_df["not_verified_posts"] = merged_df["not_verified_posts"].astype(int)
    return merged_df


if __name__ == '__main__':

    print(f'Connecting to Cassandra cluster...')
    cluster = Cluster(['0.0.0.0'], port=9042)
    session = cluster.connect('py_cassandra_ks', wait_for_all_pools=True)
    session.row_factory = lambda col_names, rows: pd.DataFrame(rows, columns=col_names)
    session.default_fetch_size = None

    # If you want to change the keyspace (It's not our case here)
    # session.set_keyspace('py_data')

    print(f'Reading data...')
    posts = pd.read_csv('data/techcrunch-posts.csv')
    posts['analyzed'] = np.where(posts['authors'].str.startswith('A'), True, False)
    print(f'"{posts.shape[0]}" posts found!')

    print(f'Saving data to Cassandra database...')
    for i, post in posts.iterrows():
        new_post(session, post)

    authors_data = calc_authors_data(posts)
    for i, author in authors_data.iterrows():
        new_author(session, author)

    print(f'"{session.execute("SELECT COUNT(*) FROM posts")._current_rows["count"].iloc[0]}" posts saved!')
    cluster.shutdown()
