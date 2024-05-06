import pandas as pd
import numpy as np
import torch
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax

file = "./data/tweets.csv"
def load_from_csv(file):
    #loading the csv file
    tweets = pd.read_csv(file)
    #removing tweets with language different than en
    tweets = tweets[tweets['language'] == 'en']
    # dropping latitude and longitude columns as there is only one row with their values
    tweets.drop(['latitude', 'longitude'], axis=1, inplace=True)
    #limiting the number of tweets due to computation time
    tweets = tweets.head(50)
    return tweets


def roberta_classifier():
    '''
        loads the csv tweets data into the pandas dataframe.
        iterates through the rows of the dataframe and calculates sentiment results for every tweet
        further joins the results for every row with the copy of original dataframe and saves the rusult as the csv file
    '''

    #loading the csv file
    tweets = pd.read_csv("/opt/airflow/dags/data/tweets.csv")
    #removing tweets with language different than en
    tweets = tweets[tweets['language'] == 'en']
    # dropping latitude and longitude columns as there is only one row with their values
    tweets.drop(['latitude', 'longitude'], axis=1, inplace=True)
    #limiting the number of tweets due to computation time
    df = tweets.head(500)
    

    # loading the roberta model 
    MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    
    
    res = {}
    try:
        for index, row in df.iterrows():
            text = row['content']
            myid = row['id']
            encoded_text = tokenizer(text, return_tensors='pt')
            output = model(**encoded_text)
            scores = output[0][0].detach().numpy()
            scores = softmax(scores)
            scores_dict = {
            'roberta_neg' : scores[0],
            'roberta_neu' : scores[1],
            'roberta_pos' : scores[2]
        }
            res[myid] = {**scores_dict}
    except RuntimeError:
        print(f'broke on {myid}')
    
    # transforming the result dictionary to pandas dataframe and merging it with the tweets data
    res_df = pd.DataFrame(res).T
    res_df = res_df.reset_index().rename(columns={'index': 'id'})
    res_df = res_df.merge(tweets, how='left')
    res_df.to_csv("/opt/airflow/dags/data/all_tweets.csv", index=False)




def load_csv_postgres(df):
    '''Separating the df into 3 new dfs based on the maximum value in the sentiment columns'''
    df = pd.read_csv("/opt/airflow/dags/all_tweets.csv")
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

    
    
        

    
# #loading the csv into pd dataframe
# tweets = load_from_csv(file)

# #loading model
# model, tokenizer = load_roberta_model()

# #performing the sentiment analysis on the loaded data
# tweets_with_sentiment = roberta_classifier(tweets)

# #saving analyzed data into CSVs 
# separate_tweets_to_csvs(tweets_with_sentiment)

