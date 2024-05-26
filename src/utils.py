import pandas as pd
import os 

def get_data():
    df=pd.read_csv('given_data/data.csv')

    print(df.head(2))

    return df
    
if __name__=="__main__":
    get_data()