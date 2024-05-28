import os 
import pandas as pd
import numpy as np
import logging
from src.components.data_ingestion import inisiate_data_ingestion

logging.basicConfig(level=logging.INFO)

def  inisiate_data_transformation(train_data_path,test_data_path):
    logging.info("Reading the train data")
    train_data=pd.read_csv(train_data_path)

    logging.info('reading test data')
    test_data=pd.read_csv(test_data_path)

    logging.info("Reading tarin and test data successfull!")
    logging.info(f"shape of train data is {train_data.shape} and shape of test data is {test_data.shape}")