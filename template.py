import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name="textSummarizer"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"

]#basically jb bhi deployment kroge toh direct github se uthaye that is why we create .github
#jb github pe commit kro toh empty folder na commit ho isliye .gitkeep....ek tareeke ki hidden file hoti ye... jb yaml file aa jyegi toh ise delete kr dege
#__init__.py is like constructor file jb bhi kch local package se import krna hota toh uske liye require hota

for filepath in list_of_files:
    filepath=Path(filepath)#create path of file
    filedir,filename=os.path.split(filepath)#config/init.py..... config ko alag aur init ko alag alag split krke ek ko folder me dal dega ek ko file me

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory:{filedir} for the file {filename} ")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"creating empty file:{filepath}")


    else:
        logging.info(f"{filename} already exists")

