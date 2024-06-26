from src.utils import get_data
from sklearn.model_selection import train_test_split
import os
import numpy as np
import logging
logging.basicConfig(level=logging.INFO)


def inisiate_data_ingestion():
    try:
        # Set the file path
        raw_path=os.path.join('data','raw','raw.csv')
        test_path=os.path.join('data','raw','test.csv')
        train_path=os.path.join('data','raw','train.csv')
        

        logging.info("Getting Data")
        df=get_data()

        logging.info("drop uncecessary columns columns are ['waterfront','sqft_above','date','street','statezip']")
        df=df.drop(columns=['waterfront','sqft_above','date','street','statezip'])

        logging.info("Replace 0 with np.nan in price col")
        df['price']=df['price'].replace(0,np.nan)

        df.dropna(inplace=True)

        logging.info("Saving the raw data")
        df.to_csv(raw_path,index=False)
        logging.info(f"Raw data save in this location {raw_path}")

        logging.info(f"Spliting the data into train and test set")
        train_set,test_set=train_test_split(df,test_size=0.2,random_state=43)

        logging.info(f"shape of train data is {train_set.shape} and {test_set.shape}")

        logging.info(f"train data save in this location {train_path}")
        train_set.to_csv(train_path,index=False)

        logging.info(f"test data save in this location {test_path}")
        test_set.to_csv(test_path,index=False)
        
        logging.info("Data ingestion Successfull")
        
        return [
            train_path,test_path
        ]
    except Exception as e:
        raise e

# print(data_ingestion())