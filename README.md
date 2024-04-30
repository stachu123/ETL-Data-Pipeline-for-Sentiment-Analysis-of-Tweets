# ETL Data Pipeline for Sentiment Analysis of Tweets
This project implements an Extract, Transform, Load (ETL) data pipeline that reads data from a CSV file containing tweets,
(Dataset can be found here: https://www.kaggle.com/datasets/mmmarchetti/tweets-dataset)
performs sentiment analysis on the data, and categorizes the tweets into three categories: positive, negative, and neutral. 
The pipeline then loads the categorized data into three separate tables in a PostgreSQL database. The project is orchestrated using Docker and Airflow.

## Project Structure
The project is organized as follows:

- data/: Contains the input CSV file with tweets.
- scripts/: Contains the Python scripts for sentiment analysis, ETL pipeline and initializing the database.
- docker-compose.yml: Docker Compose file for setting up the project environment.
- Dockerfile: Dockerfile for building the project Docker image.
- requirements.txt: Lists the Python dependencies required for the project.

## Prerequisites
Docker
Python 3.x

## Setup

1. Clone this repository to your local machine:
```
git clone https://github.com/stachu123/ETL-Data-Pipeline-for-Sentiment-Analysis-of-Tweets
```
2. Navigate to the project directory:
```bash
cd etl-data-pipeline-tweets
```
3. Build the Docker image:
```
docker build -t etl-data-pipeline-tweets .
```

## Running the Project
1. Start the project containers using Docker Compose:
```bash
docker-compose up
```
2. Access Airflow UI in your browser at http://localhost:8080 to monitor and manage the ETL pipeline. (trigger the dag)

## Airflow DAGs
The project includes Airflow DAG for orchestrating the ETL process. These DAGs are located in dags directory.

twitter_data_dag.py: Defines the ETL workflow with tasks for each step in the pipeline.

## Twitter-roBERTa-base for Sentiment Analysis

The model used for sentiment analysis in this project comes from https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment

This is a roBERTa-base model trained on ~58M tweets and finetuned for sentiment analysis with the TweetEval benchmark. This model is suitable for English (for a similar multilingual model, see XLM-T).

Reference Paper: TweetEval (Findings of EMNLP 2020): https://aclanthology.org/2020.findings-emnlp.148/
Git Repo: Tweeteval official repository: https://github.com/cardiffnlp/tweeteval



## Dbeaver

To access the data loaded into the local database, Dbeaver can be used. 
DBeaver Community is a free cross-platform database tool for developers, database administrators, analysts, and everyone working with data. 
It supports all popular SQL databases like MySQL, MariaDB, PostgreSQL, SQLite, Apache Family, and more.

To establish connection with the database:
1. Install Dbeaver program.
2. establish new Database connection and type in the credentials found in the Docker-compose file.
   
![image](https://github.com/stachu123/ETL-Data-Pipeline-for-Sentiment-Analysis-of-Tweets/assets/100467155/12728d51-aaa1-479f-8bf1-170c4d1bdf9f)
