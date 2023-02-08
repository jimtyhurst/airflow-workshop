from datetime import timedelta, datetime

from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago 


def brush_teeth():
    """A very simple python function to call"""
    print(f"calling brush_teeth function")

def toast_bread():
    """A very simple python function to call"""
    print(f"calling toast_bread function")

def butter_toast():
    """A very simple python function to call"""
    print(f"calling butter_toast function")


with DAG(
    dag_id='02_morning',
    description='A simple DAG for our morning routine',
    start_date=days_ago(2),                 # when to start running this DAG
    schedule_interval=timedelta(days=1),    # how often to run this DAG
    catchup=False,                          # do NOT catch up on previously skipped tasks
    is_paused_upon_creation=True,           # paused by default
) as dag:

    alarm_task = BashOperator(
        task_id='alarm',
        bash_command='echo "RIIIINGGG" ',
    )

    snooze_task = BashOperator(
        task_id='snooze',
        bash_command='echo "snoozing" && sleep 4',
    )

    alarm_task2 = BashOperator(
        task_id='alarm2',
        bash_command='echo "RIIIINGGG" ',
    )

    # Define the tasks for brushing teeth, toasting bread, and buttering toast here
    # They'll be PythonOperators:

    # Set the task order here:
    
