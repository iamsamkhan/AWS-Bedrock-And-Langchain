import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "AWS Bedrock And Langchain"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"AWS_Bedrock/{project_name }/app.py",
    f"AWS_Bedrock/{project_name }/claude.py",
    f"AWS_Bedrock/{project_name }/llama2.py",
    f"AWS_Bedrock/{project_name }/config/__init__.py",
    f"AWS_Bedrock/{project_name }/stablediffusion.py",
    
    "requirements.txt",
    "setup.py",
    "test.jason",
    "templates/index1.html"


]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")