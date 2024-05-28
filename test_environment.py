from src.utils import get_data
from src.components.data_ingestion import  inisiate_data_ingestion
# from src.components.data_transformation import inisiate_data_transformation
from src.components.handle_outlier import  inisiate_outliers


if __name__=="__main__":
    train_path,test_path=inisiate_data_ingestion()  
    inisiate_outliers(train_data_path=train_path,test_data_path=test_path)