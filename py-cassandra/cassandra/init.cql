-- ----------------------------------------------------------------- --
--  KEYSPACE                                                         --
-- ----------------------------------------------------------------- --
CREATE KEYSPACE py_cassandra_ks WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 2};
USE py_cassandra_ks;

-- ----------------------------------------------------------------- --
--  TBL POSTS                                                        --
-- ----------------------------------------------------------------- --
CREATE TABLE IF NOT EXISTS py_cassandra_ks.posts (
    id text,
    authors text,
    date text,
    analyzed boolean,
    category text,
    content text,
    img_src text,
    section text,
    tags text,
    title text,
    topics text,
    url text,
    PRIMARY KEY(id, analyzed, date, authors)
) WITH CLUSTERING ORDER BY(analyzed ASC, date DESC);

-- ----------------------------------------------------------------- --
--  TBL AUTHORS                                                      --
-- ----------------------------------------------------------------- --
CREATE TABLE IF NOT EXISTS py_cassandra_ks.authors (
    author text,
    verified_posts int,
    not_verified_posts int,
    PRIMARY KEY(author, verified_posts, not_verified_posts)
);
