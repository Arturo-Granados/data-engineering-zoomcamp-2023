from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from random import randint


@task(retries=3)
def fetch(dataset_url: str) -> pd.DataFrame:
    """Read taxi data from web into pandas DataFrame"""

    df = pd.read_csv(dataset_url, low_memory= False)
    return df


@task(log_prints=True) 
def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Transform data into datetime type"""

    df["lpep_pickup_datetime"] = pd.to_datetime(df["lpep_pickup_datetime"])
    df["lpep_dropoff_datetime"] = pd.to_datetime(df["lpep_dropoff_datetime"])
    
    print(f"rows: {len(df)}")
    return df


@task()
def write_local(df: pd.DataFrame, color: str, dataset_file: str) -> Path:
    """Write DataFrame out locally as parquet file"""

    path = Path(f"/home/arturo/data-engineering-zoomcamp-2023/Week 2 Homework/data/{color}/{dataset_file}.parquet")
    df.to_parquet(path, compression="gzip")
    return path


@task()
def write_gcs(path: Path) -> None:
    """Upload local parquet file to GCS"""
    gcs_block = GcsBucket.load("zoom-gcs")
    gcs_block.upload_from_path(from_path=path, to_path= 'prefect-de--zoomcamp/data')
    return


@flow(log_prints=True)
def etl_web_to_gcs(color='green', year=2020, month=1) -> None:
    """The main ETL function"""
    dataset_file = f"{color}_tripdata_{year}-{month:02}"
    dataset_url = f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{color}/{dataset_file}.csv.gz"
    df = fetch(dataset_url)
    df_clean = clean(df)
    print(f'Processed rows: {len(df_clean)}')
    path = write_local(df_clean, color, dataset_file)
    write_gcs(path)

if __name__ == "__main__":
    etl_web_to_gcs()