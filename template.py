import os 
from pathlib import Path

src_folder  = 'src'

list_of_files = [

    f"{src_folder}/__init__.py",
    f"{src_folder}/components/__init__.py",
    f"{src_folder}/components/data_ingestion.py",  
    f"{src_folder}/components/data_validation.py",
    f"{src_folder}/components/data_transformation.py",
    f"{src_folder}/components/model_trainer.py",
    f"{src_folder}/components/model_evaluation.py",
    f"{src_folder}/components/model_pusher.py",
    f"{src_folder}/configuration/__init__.py",
    f"{src_folder}/configuration/mongo_db_connection.py",
    f"{src_folder}/configuration/aws_connection.py",
    f"{src_folder}/cloud_storage/__init__.py",
    f"{src_folder}/cloud_storage/aws_storage.py",
    f"{src_folder}/data_access/__init__.py",
    f"{src_folder}/data_access/proj1_data.py",
    f"{src_folder}/constants/__init__.py",
    f"{src_folder}/entity/__init__.py",
    f"{src_folder}/entity/config_entity.py",
    f"{src_folder}/entity/artifact_entity.py",
    f"{src_folder}/entity/estimator.py",
    f"{src_folder}/entity/s3_estimator.py",
    f"{src_folder}/exception/__init__.py",
    f"{src_folder}/logger/__init__.py",
    f"{src_folder}/pipline/__init__.py",
    f"{src_folder}/pipline/training_pipeline.py",
    f"{src_folder}/pipline/prediction_pipeline.py",
    f"{src_folder}/utils/__init__.py",
    f"{src_folder}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "pyproject.toml",
    "config/model.yaml",
    "config/schema.yaml",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)
    if filedir != '':
        os.makedirs(filedir,exist_ok=True)
    if (not os.path.exists(filepath) or (os.path.getsize == 0)):
        with open(filepath,'w') as f:
            pass
    else:
        print(f"file already exist : {filepath}")