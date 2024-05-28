import pandas as pd
import os 
import logging
logging.basicConfig(level=logging.INFO)

# Getting data
def get_data():
    """
    This fun is responsible for getting data
    """
    logging.info("Reading data ......")
    df=pd.read_csv('given_data/data.csv')
    logging.info("Reading Data successfully!")
 
    return df

def drop_less_count(df,col_list):
    """ 
    This fun is responsible for handling the less count value in bedroom and bathroom
    """
    for col in col_list:
        if(col not in df.columns):
            raise f"{col} not in your dataframe"
        else:
            bedroom_counts=df[col].value_counts()
            bedroom_index=bedroom_counts[bedroom_counts>=15].index
            df=df[df[col].isin(bedroom_index)]
    return df


def winserization(df,col_list):
    """
    This fun is responsible for handling outliers using percentile approach
    """
    for col in col_list:
        if col not in df.columns:
            raise f"{col} not in dataframe"
        else:
            lower=df[col].quantile(0.01)
            upper=df[col].quantile(0.99)
            
            logging.info(f"{col} lower bound {lower} and upper bound {upper}")
            df[col]=df[col].clip(lower=lower,upper=upper)
        
    return df[col_list]
