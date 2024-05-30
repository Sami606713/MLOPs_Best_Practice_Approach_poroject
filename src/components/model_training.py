import os
import pandas as pd
import logging
from src.components.data_transformation import inisiate_data_transformation
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
# from xgboost import XGBRegressor
from src.utils import evulation_matrix
logging.basicConfig(level=logging.INFO)

def inisiate_model_trainer(train_array,test_array):
    # try:
        logging.info("Train Test split")
        x_train=train_array[:,:-1]
        y_train=train_array[:,-1]

        x_test=train_array[:,:-1]
        y_test=train_array[:,-1]
        logging.info("Saperate train and test data successfully")

        models={
            "Linear_Regression":LinearRegression(),
            "RandomForest":RandomForestRegressor(),
            "DecessionTree":DecisionTreeRegressor()
        }

        report:dict=evulation_matrix(x_train=x_train,y_train=y_train,x_test=x_test,y_test=y_test,models=models)
        max_score=sorted(report.values(),reverse=True)
        print(max_score)

        best_model=dict(sorted(report.items(), key=lambda item: item[1], reverse=True))
        print(best_model)
        

    # except Exception as e:
    #     return e
    

    