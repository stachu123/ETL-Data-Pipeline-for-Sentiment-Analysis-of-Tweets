import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# def connect_to_database():


def load_csv_postgres():
    """ dedicated to loading the data from csv file into postgres sql"""

    #creating connection to the local databae
    engine = create_engine('postgresql+psycopg2://airflow:airflow@host.docker.internal:54321/postgres')
    connection = engine.connect()

    #Separating the df into 3 new dfs based on the maximum value in the sentiment columns
    df = pd.read_csv("/opt/airflow/dags/data/all_tweets.csv")
    # df = pd.read_csv("dags/all_tweets.csv")
    df.drop(['country', 'language'], axis=1, inplace=True)
    df['date_time'] = pd.to_datetime(df['date_time'], format='%d/%m/%Y %H:%M')
    unique_ids = [_ for _ in range(len(df))]
    df["id"] = unique_ids
    pos_tweets = pd.DataFrame()
    neu_tweets = pd.DataFrame()
    neg_tweets = pd.DataFrame()
    
    #loading data into 3 dfs basing on the max value in sentiment columns 
    for index, row in df.iterrows():
        if row['roberta_neg'] > row['roberta_pos'] and row['roberta_neg'] > row['roberta_neu']:
            neg_tweets = pd.concat([neg_tweets, pd.DataFrame(row).T], ignore_index=True)
        elif row['roberta_pos'] > row['roberta_neg'] and row['roberta_pos'] > row['roberta_neu']:
            pos_tweets = pd.concat([pos_tweets, pd.DataFrame(row).T], ignore_index=True)
        else:
            neu_tweets = pd.concat([neu_tweets, pd.DataFrame(row).T], ignore_index=True)

    

    #loading the data
    pos_tweets.to_sql('positive_tweets', engine, if_exists='append', index=False)
    neu_tweets.to_sql('neutral_tweets', engine, if_exists='append', index=False)
    neg_tweets.to_sql('negative_tweets', engine, if_exists='append', index=False)


    # Close the connection
    connection.close()

