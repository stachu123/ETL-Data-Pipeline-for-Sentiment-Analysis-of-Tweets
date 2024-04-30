CREATE TABLE IF NOT EXISTS positive_tweets (
    id SERIAL PRIMARY KEY,
    roberta_neg NUMERIC,
    roberta_neu NUMERIC,
    roberta_pos NUMERIC,
    author VARCHAR(50),
    content TEXT,
    date_time TIMESTAMP,
    number_of_likes INTEGER,
    number_of_shares INTEGER
);

CREATE TABLE IF NOT EXISTS negative_tweets (
    id SERIAL PRIMARY KEY,
    roberta_neg NUMERIC,
    roberta_neu NUMERIC,
    roberta_pos NUMERIC,
    author VARCHAR(50),
    content TEXT,
    date_time TIMESTAMP,
    number_of_likes INTEGER,
    number_of_shares INTEGER
);

CREATE TABLE IF NOT EXISTS neutral_tweets (
    id SERIAL PRIMARY KEY,
    roberta_neg NUMERIC,
    roberta_neu NUMERIC,
    roberta_pos NUMERIC,
    author VARCHAR(50),
    content TEXT,
    date_time TIMESTAMP,
    number_of_likes INTEGER,
    number_of_shares INTEGER
);

TRUNCATE TABLE positive_tweets;
TRUNCATE TABLE negative_tweets;
TRUNCATE TABLE neutral_tweets;

