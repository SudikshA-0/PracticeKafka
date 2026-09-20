from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator


# Task 1: Collect metrics
def collect_metrics():
    metrics = {
        "server_id": "server01",
        "cpu_usage": 95,
        "memory_usage": 70
    }

    print("Collected metrics:", metrics)


# Task 2: Process metrics
def process_metrics():
    print("Processing server metrics...")
    print("Metrics processed successfully.")


# Task 3: Detect anomaly
def detect_anomaly():
    cpu_usage = 95

    if cpu_usage > 80:
        print("ANOMALY DETECTED: High CPU usage")
    else:
        print("No anomaly detected.")


# Task 4: Generate report
def generate_report():
    print("Generating final AIOps report...")
    print("Report generated successfully.")


# Create DAG
with DAG(
    dag_id="aiops_monitoring_dag",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    collect_task = PythonOperator(
        task_id="collect_metrics",
        python_callable=collect_metrics,
    )

    process_task = PythonOperator(
        task_id="process_metrics",
        python_callable=process_metrics,
    )

    detect_task = PythonOperator(
        task_id="detect_anomaly",
        python_callable=detect_anomaly,
    )

    report_task = PythonOperator(
        task_id="generate_report",
        python_callable=generate_report,
    )

    # Task dependencies
    collect_task >> process_task >> detect_task >> report_task