from datetime import datetime, timedelta
from airflow import  DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python_operator import PythonOperator

from scripts.load_to_postgres import load_csv_postgres 
from scripts.extract_transform import  roberta_classifier

default_args = {
    'owner': 'stan',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id = 'tweets_dag',
    default_args=default_args,
    start_date=datetime.today(),
    schedule_interval='@daily'
) as dag:

    initialize_database_task = PostgresOperator(
        task_id = 'init_tweets_db',
        postgres_conn_id='postgres_database',
        sql = "./scripts/init_db.sql"
    )

    execute_python_script_task = PythonOperator(
    task_id='execute_python_script',
    python_callable= roberta_classifier
)
    connect_to_database = PythonOperator(
    task_id='connect_to_database',
    python_callable= load_csv_postgres
)

    initialize_database_task >> execute_python_script_task >> connect_to_database
