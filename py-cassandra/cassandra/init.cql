-- ----------------------------------------------------------------- --
--  KEYSPACE                                                         --
-- ----------------------------------------------------------------- --
create keyspace py_data with replication = {'class': 'SimpleStrategy', 'replication_factor': 2};
USE py_data;

-- ----------------------------------------------------------------- --
--  TBL POSTS                                                        --
-- ----------------------------------------------------------------- --
CREATE TABLE posts (
    id int, author text, title text, content text, published_at timestamp,
    PRIMARY KEY(id, published_at, author)
) WITH CLUSTERING ORDER BY(published_at DESC, author ASC);

-- ----------------------------------------------------------------- --
--  POSTS                                                            --
-- ----------------------------------------------------------------- --
INSERT INTO posts(id, author, title, content, published_at) VALUES (1, 'anthony', 'Post 01', 'Content 01', toTimestamp(now()));
INSERT INTO posts(id, author, title, content, published_at) VALUES (2, 'joe',     'Post 02', 'Content 02', toTimestamp(now()));
INSERT INTO posts(id, author, title, content, published_at) VALUES (3, 'nina',    'Post 03', 'Content 03', toTimestamp(now()));
