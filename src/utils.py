import pandas as pd
import os 
import logging
logging.basicConfig(level=logging.INFO)

def get_data():
    logging.info("Reading data ......")
    df=pd.read_csv('given_data/data.csv')
    logging.info("Reading Data successfully!")

    return df
    
if __name__=="__main__":
    get_data()