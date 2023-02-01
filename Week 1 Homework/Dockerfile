FROM python:3.9

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app
COPY data_ingestion.py data_ingestion.py

ENTRYPOINT [ "python", "data_ingestion.py" ]








