import os 
import pandas as pd
import numpy as np
import logging
from src.components.data_ingestion import inisiate_data_ingestion
from src.utils import winserization,drop_less_count

logging.basicConfig(level=logging.INFO)

def  inisiate_outliers(train_data_path,test_data_path):
    train_process_data_path=os.path.join("data","process",'train_process.csv')
    test_process_data_path=os.path.join("data","process",'test_process.csv')
    

    logging.info("Reading the train data")
    train_data=pd.read_csv(train_data_path)
    
    logging.info('reading test data')
    test_data=pd.read_csv(test_data_path)
    # print(test_data.isnull().sum())

    logging.info("Reading tarin and test data successfull!")
    logging.info(f"shape of train data is {train_data.shape} and shape of test data is {test_data.shape}")


    columns_list=['price','sqft_living','sqft_lot','sqft_basement']

    logging.info("Applyig winserization on train data")
    train_data[columns_list]=winserization(train_data,col_list=columns_list)
    logging.info("winserization successfully apply on train data")

    logging.info("Applyig winserization on test data")
    test_data[columns_list]=winserization(test_data,col_list=columns_list)
    logging.info("winserization successfully apply on test data")

    logging.info("handle less count value in train data")
    cat_col_list=['bedrooms','bathrooms']
    logging.info("handle outleirs on train data")
    train_data_process=drop_less_count(df=train_data,col_list=cat_col_list)

    logging.info("handle outleirs on test data")
    test_data_process=drop_less_count(df=test_data,col_list=cat_col_list)

    logging.info("saving the process data")
    logging.info(f"train data process save in this path {train_process_data_path}")
    train_data_process.to_csv(train_process_data_path,index=False)

    logging.info(f"test data process save in this path {test_process_data_path}")
    test_data_process.to_csv(test_process_data_path,index=False)
 
    return [
        train_process_data_path,
        test_process_data_path
    ]



    