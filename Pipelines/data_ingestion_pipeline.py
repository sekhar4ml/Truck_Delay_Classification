import pandas as pd
from components.data_ingestion import DataIngestion
from constants import *
import joblib
import os
STAGE_NAME = "Data Ingestion"

class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            ingestion = DataIngestion()
            ingestion.connect()
            data = ingestion.read_all_tables()
            joblib.dump(data, './Data/DataFrame/dataframes_dict.joblib')
            
            ingestion.close_connection()
            
        except Exception as e:
            print(f"An error occurred: {e}")
            raise e

    
if __name__ == '__main__':
    try:
        print(">>>>>> Stage started <<<<<< :",STAGE_NAME)
        obj = DataIngestionPipeline()
        obj.main()
        print(">>>>>> Stage completed <<<<<<", STAGE_NAME)
    except Exception as e:
        print(e)
        raise e