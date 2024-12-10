from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.hooks.base import BaseHook
from datetime import datetime
import smtplib
import pandas as pd
import csv


def send_email():
    # Fetch the SMTP connection from Airflow
    # Replace 'smtp_default' with your Connection ID if different
    conn = BaseHook.get_connection('smtp_default')

    smtp_server = conn.host
    port = conn.port
    sender_email = conn.login
    password = conn.password
    recipient_email = "robel_tewelde@hotmail.com"  # Update recipient as necessary

    # Send the email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls()  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        print("Login successful")
        server.sendmail(sender_email, recipient_email, "Test message")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()


# Define the DAG
with DAG(
    dag_id='smtp_email_dag',
    start_date=datetime(2023, 9, 1),
    # Set your desired schedule interval (e.g., '@daily')
    schedule_interval=None,
    catchup=False
) as dag:

    send_email_task = PythonOperator(
        task_id='send_email',
        python_callable=send_email
    )
