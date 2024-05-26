from src.utils import get_data
from src.components.data_ingestion import  inisiate_data_ingestion

if __name__=="__main__":
    train_path,test_path=inisiate_data_ingestion()
    print(train_path)
    print(test_path)