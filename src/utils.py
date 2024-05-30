import pandas as pd
import pickle as pkl
from sklearn.metrics import r2_score
from sklearn.model_selection import cross_val_score
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

def save_file(obj,file_path):
    """
    This fun is responsible for saving the pickle file in specific location
    """
    with open(file_path,'wb') as f:
        pkl.dump(obj,f)


def evulation_matrix(x_train,y_train,x_test,y_test,models):
    print("Data Found Successfully")
    full_report={
        "model":[],
        "train_score":[],
        "test_score":[],
        "train_cv":[],
        "test_cv":[]
    }

    report={}
    for name, model in models.items():
        
        model.fit(x_train,y_train)
        logging.info(f'{model} train')

        logging.info(f"test prediction")
        test_pre=model.predict(x_test)
        test_score=r2_score(y_test,test_pre)

        logging.info(f"train prediction")
        train_pre=model.predict(x_train)

        train_score=r2_score(y_train,train_pre)
        report[model]=test_score

        # train_cross_validation
        train_cv_score=cross_val_score(model,x_train,y_train,cv=5).mean()

        # test_cross_validation
        test_cv_score=cross_val_score(model,x_test,y_test,cv=5).mean()

        # full_report["model"].append(model)
        # full_report["train_score"].append(train_score)
        # full_report["test_score"].append(test_score)
        # full_report["train_cv"].append(train_cv_score)
        # full_report["test_cv"].append(test_cv_score)
        
    # df=pd.DataFrame(full_report)
    # print(df)
        
    return report
        