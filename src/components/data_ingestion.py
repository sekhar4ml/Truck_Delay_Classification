import psycopg2
import pandas as pd
from constants import *



class DataIngestion:
    def __init__(self):
        self.db_config = DB_CONFIG
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(**self.db_config)
            print("Connection to PostgreSQL successful")
        except psycopg2.Error as e:
            print(f"Error connecting to PostgreSQL: {e}")

    def read_table(self, table_name):
        if self.connection is None:
            raise Exception("Database not connected.")
        
        query = f"SELECT * FROM {table_name}"
        return pd.read_sql_query(query, self.connection)

    def read_all_tables(self):
        if self.connection is None:
            raise Exception("Database not connected.")
        
        cursor = self.connection.cursor()
        
        cursor.execute(
            """
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public';
            """
        )
        
        tables = cursor.fetchall()
        data = {}
        for table_name in tables:
            data[table_name[0]] = self.read_table(table_name[0])
        
        return data
    
    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection closed.")
