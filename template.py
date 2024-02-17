import os

# Path => path customization based on OS
# windows => backword slash (\)
# Linux => forward slash => (/)
from pathlib import Path
import logging

# logging level => INFO
# logging format => ascii time: message
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# main project folder under src folder
project_name = "TextSummarizer"

# nested files and folders/local modules list
list_of_files = [
    # .github => cloud deployment
    # CI/CD, config YAML, auto deployment upon code commit 
    ".github/workflows/.gitkeep",

    # src => root project folder
    # __init__ constructor file => making a folder as local python package
    f"src/{project_name}/__init__.py",

    # conponents folder => another local package 
    f"src/{project_name}/conponents/__init__.py",

    # utils => unility local package
    f"src/{project_name}/utils/__init__.py",
    # common.py => contains utility code
    f"src/{project_name}/utils/common.py",

    # logging => local package
    f"src/{project_name}/logging/__init__.py",

    # config => local package
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",

    # pipeline => local module
    # training and prediction pipe lines
    f"src/{project_name}/pipeline/__init__.py",

    # pipeline => local module    
    f"src/{project_name}/entity/__init__.py",

    # pipeline => local module
    f"src/{project_name}/constants/__init__.py",

    "config/config.yaml",
    
    # params.yaml => model related parameters
    "params.yaml",

    "app.py",
    "main.py",
    
    # Dockerfile => docker image for deployment 
    "Dockerfile",

    "requirements.txt",

    # setup.py => local package setup 
    "setup.py",

    # research => contains all notebook experiments 
    "research/trials.ipynb",
]

for filepath in list_of_files:
    # path customization
    filepath = Path(filepath)

    # splits the file and folders on specified path
    # need to create folders and files separately
    filedir, filename = os.path.split(filepath)

    # check => if there is a folder in the specified path 
    if filedir != "":
        # exist_ok=True => if folder is there do not override/re-create
        os.makedirs(filedir, exist_ok=True)
        # folder created
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    # check => file does not exist or file size 0
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # just create the file only
        with open(filepath,'w') as f:
            pass
            # file created
            logging.info(f"Creating empty file: {filepath}")
    # file exist
    else:
        logging.info(f"{filename} is already exists")


