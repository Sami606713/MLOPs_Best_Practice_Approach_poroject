# Automate Data Science Life Cycle
**In this repo i will do project using MLOPS way the goal of this project is to understand how we can do project using mlops approach i am not focing on best results.**
- # Tool use for model and data version
 - ![MLflow](https://github.com/Sami606713/MLOPs_Best_Practice_Approach_poroject/assets/123552889/261b09ca-23fc-4e8b-8a03-bfadf8fcc24f)
 - ![DVC]() DVC (For Version Control)

## Directory and File Descriptions

### data/
- **raw/**: Directory to store raw data.
- **process/**: Directory to store processed data.

### src/
- **\_\_init\_\_.py**: Initializes the src module.
- **utils.py**: Utility functions.
- **components/**: Contains all the component modules.
  - **\_\_init\_\_.py**: Initializes the components module.
  - **data_ingestion.py**: Module for data ingestion.
  - **handle_outlier.py**: Module for handling outliers.
  - **data_transformation.py**: Module for data transformation.
  - **model_training.py**: Module for model training.
  - **data_monetring.py**: Module for data monitoring.
- **pipeline/**: Contains the pipeline scripts.
  - **\_\_init\_\_.py**: Initializes the pipeline module.
  - **training_pipeline.py**: Script for training pipeline.
  - **prediction_pipeline.py**: Script for prediction pipeline.

### notebook/
- Directory for Jupyter notebooks.

### models/
- Directory to save trained models.

### report/
- Directory to save reports and results.

### Other Files
- **README.md**: This file, providing an overview of the project.
- **requirements.txt**: List of Python dependencies.
- **.env**: Environment variable configuration file.
- **test_environment.py**: Script to test the environment setup.
- **app.py**: Script for web code .
- **Dockerfile**: For containerize the code .
- **.dockerignore**: Files and directories to ignore in Docker builds.### Getting Started
1. Clone the repository:
    ```sh
    git clone https://github.com/Sami606713/MLOPs_Best_Practice_Approach_poroject/
    ```
2. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the application:
    ```sh
    python test_environment.py
    ```
4. Run web application:
    ```sh
     streamlit run app.py
    ```
