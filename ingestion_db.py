import pandas as pd
import os
from sqlalchemy import create_engine
import time
import logging

#logging.basicConfig(
 #   filename="logs/ingestion_db.log",
 #   level=logging.DEBUG,
 #   format="%(asctime)s-%(message)s",
 #   filemode="a"    
#)

logger = logging.getLogger("ingestion_db")  # custom logger
logger.setLevel(logging.DEBUG)

# Optional: prevent duplication if handler already exists
if not logger.handlers:
    fh = logging.FileHandler("logs/ingestion_db.log")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    fh.setFormatter(formatter)
    logger.addHandler(fh)


engine = create_engine('sqlite:///inventory.db')

''' This function will ingest dataframe into DB table'''
def ingest_db(df, table_name, engine):
    df.to_sql(table_name, con=engine, if_exists='replace', index=False, chunksize=10000)

def load_raw_data():
    ''' This function will load data from CSV and Ingest it into DB'''
    start=time.time()
    for file in os.listdir('data'):
        if '.csv' in file:
            df=pd.read_csv('data/'+file, low_memory=True)
            logger.info(f'Ingesting {file} in db')
            ingest_db(df, file[:-4],engine)
    end=time.time()
    total_time=(end-start)/60
    logger.info("--------Ingestion Complete-----------")
    logger.info(f'\n Total Time taken :{total_time} minutes')
    
if __name__=='__main__':
    load_raw_data()