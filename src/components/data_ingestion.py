from src.utils import get_data
from sklearn.model_selection import train_test_split
import os
import logging
logging.basicConfig(level=logging.INFO)


def inisiate_data_ingestion():
    # Set the file path
    raw_path=os.path.join('data','raw','raw.csv')
    test_path=os.path.join('data','raw','test.csv')
    train_path=os.path.join('data','raw','train.csv')
    

    logging.info("Getting Data")
    df=get_data()

    logging.info("Saving the raw data")
    df.to_csv(raw_path,index=False)
    logging.info(f"Raw data save in this location data/raw")

    logging.info(f"Spliting the data into train and test set")
    train_set,test_set=train_test_split(df,test_size=0.2,random_state=43)

    logging.info(f"train data save in this location {train_path}")
    train_set.to_csv(train_path,index=False)

    logging.info(f"test data save in this location {test_path}")
    train_set.to_csv(test_path,index=False)
    
    logging.info("Data ingestion Successfull")
    
    return [
        train_path,test_path
    ]


# print(data_ingestion())