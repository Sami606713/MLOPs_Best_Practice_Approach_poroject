import os
import logging
logging.basicConfig(level=logging.INFO)
# Make the folder structure
project_name="ml_project"
dirs=[
    os.path.join("data","raw"),
    os.path.join("data","process"),
    os.path.join("src",project_name),
    os.path.join(f"src/{project_name}",'components'),
    os.path.join(f"src/{project_name}","pipeline"),
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
    os.path.join(f"src/{project_name}","__init__.py"),
    os.path.join(f"src/{project_name}","utils.py"),

    os.path.join(f"src/{project_name}/components","__init__.py"),
    os.path.join(f"src/{project_name}/components","data_ingestion.py"),
    os.path.join(f"src/{project_name}/components","data_transformation.py"),
    os.path.join(f"src/{project_name}/components","model_training.py"),
    os.path.join(f"src/{project_name}/components","data_monetring.py"),

    os.path.join(f"src/{project_name}/pipeline","__init__.py"),
    os.path.join(f"src/{project_name}/pipeline","training_pipeline.py"),
    os.path.join(f"src/{project_name}/pipeline","prediction_pipeline.py"),
    "README.md",
    "requirements.txt",
    ".env"    
]

for file in files:
    if(not os.path.exists(file)) or (os.path.getsize(file)==0):

        with open(file,"w") as f:
            pass
    else:
        logging.info(f"File {file} already exists")