import os
import logging
logging.basicConfig(level=logging.INFO)
# Make the folder structure

dirs=[
    os.path.join("data","raw"),
    os.path.join("data","process"),
    os.path.join(f"src",'components'),
    os.path.join(f"src","pipeline"),
    "notebook",
    "models"
]

for dir_ in dirs:
    if not os.path.exists(dir_):
        os.makedirs(dir_,exist_ok=True)

        # add a gitkeep file

        git_keep=os.path.join(dir_,".gitkeep")

        with open(git_keep,"w") as f:
            pass

# Make the files

files=[
    os.path.join(f"src","__init__.py"),
    os.path.join(f"src","utils.py"),

    os.path.join(f"src/components","__init__.py"),
    os.path.join(f"src/components","data_ingestion.py"),
    os.path.join(f"src/components","handle_outlier.py"),
    os.path.join(f"src/components","data_transformation.py"),
    os.path.join(f"src/components","model_training.py"),
    os.path.join(f"src/components","data_monetring.py"),

    os.path.join(f"src/pipeline","__init__.py"),
    os.path.join(f"src/pipeline","training_pipeline.py"),
    os.path.join(f"src/pipeline","prediction_pipeline.py"),
    "README.md",
    "requirements.txt",
    ".env",   
    "test_environment.py"
]

for file in files:
    if(not os.path.exists(file)) or (os.path.getsize(file)==0):

        with open(file,"w") as f:
            pass
    else:
        logging.info(f"File {file} already exists")