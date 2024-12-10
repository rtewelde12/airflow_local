from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Function to execute


def hello_world():
    print("Hello, World!")


# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
}

# Define the DAG
with DAG(
    dag_id='hello_world_dag',
    default_args=default_args,
    schedule_interval='@daily',  # Change to your desired schedule
    catchup=False,  # Avoid running past DAGs
) as dag:
    # Define a task using the PythonOperator
    hello_task = PythonOperator(
        task_id='hello_task',
        python_callable=hello_world,
    )
