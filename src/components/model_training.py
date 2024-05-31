from src.components.data_transformation import inisiate_data_transformation
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from src.utils import evulation_matrix,save_file,save_report
import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO)

def inisiate_model_trainer(train_array,test_array):
    try:
        # path whre model should be save
        model_path=os.path.join("models","best_model.pkl")

        # Full report path
        report_path=os.path.join("report","model_report.json")

        logging.info("Train Test split")
        x_train=train_array[:,:-1]
        y_train=train_array[:,-1]

        x_test=test_array[:,:-1]
        y_test=test_array[:,-1]
        logging.info("Saperate train and test data successfully")

        models={
            "Linear_Regression":LinearRegression(),
            "RandomForest":RandomForestRegressor(),
            "DecessionTree":DecisionTreeRegressor(),
            "Xgboost":XGBRegressor()
        }

        report ,full_report=evulation_matrix(x_train=x_train,y_train=y_train,x_test=x_test,y_test=y_test,models=models)
        logging.info("Saving the full report")
        save_report(file=full_report,file_path=report_path)

        best_model_name = max(report, key=report.get)
        best_model_score = sorted(report.values(),reverse=True)[0]
        if(best_model_score>0.50):
            print("Best model is: ",best_model_name," Score is :",best_model_score)

            logging.info("Saving the model...")
            save_file(obj=best_model_name,file_path=model_path)
            logging.info(f"{best_model_name} successfully save in this location {model_path}")
        else:
            print("Not Best model found")

    except Exception as e:
        return e
    

    