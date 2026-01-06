from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from datetime import datetime, timedelta

# Default arguments for all DAG tasks
default_args = {
    "owner": "agriculture_analytics",
    "depends_on_past": False,
    
    # Retry failed tasks twice
    "retries": 2,       
    
    # Wait time between retries              
    "retry_delay": timedelta(minutes=5)  
}

with DAG(
    # DAG name
    dag_id="agriculture_pipeline_dag",     
    default_args=default_args,
    
    # DAG start date
    start_date=datetime(2024, 1, 1), 
    
    # Daily execution   
    schedule_interval="@daily",      
       
    # Do not backfill past runs
    catchup=False,                      
    tags=["agriculture", "databricks", "etl"]
) as dag:

    # Trigger Databricks bronze layer job
    bronze = DatabricksRunNowOperator(
        task_id="bronze_job",
        databricks_conn_id="databricks_default",
        job_id=89140600327455
    )

    # Trigger Databricks silver layer job
    silver = DatabricksRunNowOperator(
        task_id="silver_job",
        databricks_conn_id="databricks_default",
        job_id=89140600327455
    )

    # Trigger Databricks gold layer job
    gold = DatabricksRunNowOperator(
        task_id="gold_job",
        databricks_conn_id="databricks_default",
        job_id=89140600327455
    )

    # Define execution order
    bronze >> silver >> gold
