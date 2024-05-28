from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder,FunctionTransformer
from sklearn.compose import ColumnTransformer
from src.utils import save_file
import numpy as np
import pandas as pd
import os
import logging
logging.basicConfig(level=logging.INFO)

def inisiate_data_transformation(train_process_path,test_process_path):
    try:
        # set the path to save the processor as a pkl
        pkl_file_path=os.path.join("models","processor.pkl")

        train_df=pd.read_csv(train_process_path)
        test_df=pd.read_csv(test_process_path)

        # Saperate the Feature and label
        x_train=train_df.drop(columns=['price'])
        y_train=train_df['price']
        x_test=test_df.drop(columns=['price'])
        y_test=test_df['price']

        num_col=x_train.select_dtypes('number').columns
        cat_col=x_train.select_dtypes('object').columns

        # Building Numerical Pipeline
        num_pipe=Pipeline(steps=[
            ("impute",SimpleImputer(strategy='mean')),
            ("fun transformer",FunctionTransformer(func=np.log1p)),
            ("scale",StandardScaler())
        ])

        # Building Categorical Pipeline
        cat_pipe=Pipeline(steps=[
            ("impute",SimpleImputer(strategy="most_frequent")),
            ("encode",OneHotEncoder(drop='first',sparse_output=False,handle_unknown='ignore',))
        ])

        # Building Transformer
        process=ColumnTransformer(transformers=[
            ('num_transform',num_pipe,num_col),
            ("cat_transform",cat_pipe,cat_col)
        ],remainder='passthrough')

        # Apply the transformation
        x_train_transform=process.fit_transform(x_train)
        x_test_transform=process.transform(x_test)

        # Combine the transform data with target columns
        train_array=np.c_[
            x_train_transform,np.array(y_train)
        ]

        test_array=np.c_[
            x_test_transform,np.array(y_test)
        ]

        # save the processor
        logging.info("saving the processor")
        save_file(obj=process,file_path=pkl_file_path)
        logging.info(f"processor save in this location {pkl_file_path}")

        return [
            train_array,
            test_array,pkl_file_path
        ]

        
    except Exception as e:
        raise e