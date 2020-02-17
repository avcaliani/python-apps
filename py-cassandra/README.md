# 👀 Py Cassandra
By Anthony Vilarim Caliani

[![#](https://img.shields.io/badge/licence-MIT-blue.svg)](#) [![#](https://img.shields.io/badge/python-3.7.x-yellow.svg)](#) [![#](https://img.shields.io/badge/cassandra-3.11-lightseagreen.svg)](#) 

## Description
Some experiments using _Cassandra_ database.

## Quick Start

> 👉 Before run these scripts make sure that you have installed Python 3 ;)

```bash
# Let's do it \o/
./run.sh start

# For more options type "./run.sh -h"
# After using...
./run.sh stop
```

## Trying Cassandra

> 👉 Before run these commands make sure that your Cassandra docker containers are up and running ;)

```bash
docker exec -it cassandra-node-02 cqlsh
```

```sql
-- Replication Factor is "2" because I have only 2 nodes available.
create keyspace city_info with replication = {'class': 'SimpleStrategy', 'replication_factor': 2};
USE city_info;


-- ----------------------------------------------------------------- --
-- TBL CITIES                                                        --
-- ----------------------------------------------------------------- --
CREATE TABLE cities (
    id int, name text, country text, PRIMARY KEY(id)
);

INSERT INTO cities(id,name,country) VALUES (1,'Karachi','Pakistan');
INSERT INTO cities(id,name,country) VALUES (2,'Lahore','Pakistan');
INSERT INTO cities(id,name,country) VALUES (3,'Dubai','UAE');
INSERT INTO cities(id,name,country) VALUES (4,'Berlin','Germany');


-- ----------------------------------------------------------------- --
-- TBL USERS                                                         --
-- ----------------------------------------------------------------- --
CREATE TABLE users (
    username text, name text, age int, PRIMARY KEY(username)
);

INSERT INTO users(username,name,age) VALUES ('aali24','Ali Amin',34);
INSERT INTO users(username,name,age) VALUES ('jack01','Jack David',23);
INSERT INTO users(username,name,age) VALUES ('ninopk','Nina Rehman',34);
                                                     

-- ----------------------------------------------------------------- --
-- TBL USERS BY CITIES                                               --
-- ----------------------------------------------------------------- --
CREATE TABLE users_by_cities (
    username text, name text, city text, age int, PRIMARY KEY(city,age)
);

INSERT INTO users_by_cities(username,name,city,age) VALUES ('aali24','Ali Amin','Karachi',34);
INSERT INTO users_by_cities(username,name,city, age) VALUES ('jack01','Jack David','Berlin',23);
INSERT INTO users_by_cities(username,name,city, age) VALUES ('ninopk','Nina Rehman','Lahore',34);


-- ----------------------------------------------------------------- --
-- BATCH INSERT                                                      --
-- ----------------------------------------------------------------- --
BEGIN BATCH
INSERT into users(username,name,age) VALUES('raziz12','Rashid Aziz',34);
INSERT INTO users_by_cities(username,name,city, age) VALUES ('raziz12','Rashid Aziz','Karachi',30);
APPLY BATCH;


-- ----------------------------------------------------------------- --
-- LOOKING FOR OUR DATA!                                             --
-- ----------------------------------------------------------------- --
EXPAND ON
select * from users;
-- @ Row 1
-- ----------+-------------
--  username | aali24
--  age      | 34
--  name     | Ali Amin
--          ...


select token(username) from users;
-- @ Row 1
-- ------------------------+----------------------
--  system.token(username) | -7905752472182359000
--                        ...


select token(username),username,city from users_by_cities;
-- @ Row 1
-- ------------------------+----------------------
--  system.token(username) | 2621513098312339776
--  username               | jack01
--  city                   | Berlin
--                        ...


select * from users_by_cities where city = 'Karachi';
-- @ Row 1
-- ----------+-------------
--  city     | Karachi
--  age      | 30
--  name     | Rashid Aziz
--  username | raziz12
-- 
-- @ Row 2
-- ----------+-------------
--  city     | Karachi
--  age      | 34
--  name     | Ali Amin
--  username | aali24
-- 
-- (2 rows)


select * from users_by_cities where city = 'Karachi' and age = 34;
-- @ Row 1
-- ----------+----------
--  city     | Karachi
--  age      | 34
--  name     | Ali Amin
--  username | aali24
-- 
-- (1 rows)              


-- ----------------------------------------------------------------- --
-- OOPS!!!!                                                          --
-- ----------------------------------------------------------------- --
select * from users_by_cities where name = 'Ali Amin';
-- InvalidRequest: 
--   Error from server: 
--     code=2200 [Invalid query] 
--     message="Cannot execute this query as it might involve data filtering 
--              and thus may have unpredictable performance. If you want to 
--              execute this query despite the performance unpredictability,
--              use ALLOW FILTERING"
--
-- It is because no partition key was mentioned!!! So be careful!

exit
```

## Related Links
- [DockerHub: Cassandra](https://hub.docker.com/_/cassandra)
- [Cassandra + Python (Tutorial)](https://towardsdatascience.com/getting-started-with-apache-cassandra-and-python-81e00ccf17c9)
- [Cassandra G.U.I.](https://tableplus.com/)
- [Posts Data Set](https://www.kaggle.com/thibalbo/techcrunch-posts-compilation/download)

---

_You can find [@avcaliani](#) at [GitHub](https://github.com/avcaliani) or [GitLab](https://gitlab.com/avcaliani)._
