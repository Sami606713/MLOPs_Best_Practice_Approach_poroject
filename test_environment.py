from src.utils import get_data
from src.components.data_ingestion import  inisiate_data_ingestion
from src.components.data_transformation import inisiate_data_transformation
from src.components.handle_outlier import  inisiate_outliers
from src.components.model_training import inisiate_model_trainer


if __name__=="__main__":
    train_path,test_path=inisiate_data_ingestion()  

    train_process,test_process=inisiate_outliers(train_data_path=train_path,test_data_path=test_path)

    train_arr,test_arr,_=inisiate_data_transformation(train_process_path=train_process,test_process_path=test_process)

    inisiate_model_trainer(train_array=train_arr,test_array=test_arr)