import os

# Make the folder structure
dirs=[
    os.path.join("data","raw"),
    os.path.join("data","process"),
    os.path.join("src","components"),
    os.path.join("src","pipeline"),
    "notebook",
    "models"
]

for dir_ in dirs:
    os.makedirs(dir_,exist_ok=True)

    # add a gitkeep file

    git_keep=os.path.join(dir_,".gitkeep")

    with open(git_keep,"w") as f:
        pass

# Make the files

files=[
    os.path.join("src","__init__.py"),
    os.path.join("src","utils.py"),

    os.path.join("src/components","__init__.py"),
    os.path.join("src/components","data_ingestion.py"),
    os.path.join("src/components","data_transformation.py"),
    os.path.join("src/components","model_training.py"),
    os.path.join("src/components","data_monetring.py"),

    os.path.join("src/pipeline","__init__.py"),
    os.path.join("src/pipeline","training_pipeline.py"),
    os.path.join("src/pipeline","prediction_pipeline.py"),
    "setup.py",
    "README.md",
    "requirements.txt",
    ".env"    
]

for file in files:
    with open(file,"w") as f:
        pass


def require(path):
    with open(path,"r") as f:
        print(f.read().splitlines())

require('requirements.txt')