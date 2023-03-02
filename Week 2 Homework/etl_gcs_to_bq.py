from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials
 

@task(retries=3)
def extract_from_gcs(color: str, year: int, month: int) -> Path:
    """Download trip data from GCS"""

    gcs_path = f"data/{color}/{color}_tripdata_{year}-{month:02}.parquet"
    gcs_block = GcsBucket.load("zoom-gcs")
    gcs_block.get_directory(from_path=gcs_path, local_path=f"/home/arturo/data-engineering-zoomcamp-2023/Week 2 Homework/data/")
    return Path(f"/home/arturo/data-engineering-zoomcamp-2023/Week 2 Homework/{gcs_path}")  #f"../data/{gcs_path}"
    

@task()
def transform(path: Path) ->pd.DataFrame:
    df = pd.read_parquet(path)
    return df

@task()
def write_bq(df: pd.DataFrame) -> None:
    """Write DataFrame to BiqQuery"""

    gcp_credentials_block = GcpCredentials.load("zoom-gcp-creds")
    df.to_gbq(
        destination_table="GreenTaxi.rides",
        project_id="dtc-de-376620",
        credentials=gcp_credentials_block.get_credentials_from_service_account(),
        chunksize=500_000,
        if_exists="append"
    )


@flow(log_prints=True)
def etl_gcs_to_bq(months: list[int] = [1], year: int = 2020, color: str = 'green'):
    """Main ETL flow to load data into Big Query"""

    total_rows = 0
    for month in months:
        path = extract_from_gcs(color, year, month)
        df = transform(path)
        print(f'{color} {year}-{month} rows: {len(df)}')
        total_rows += len(df)
        write_bq(df)
    print(f'Processed rows (total): {total_rows}')

if __name__ == "__main__":
    etl_gcs_to_bq()