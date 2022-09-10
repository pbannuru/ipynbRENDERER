import os
import pathlib  # this makes application os independent of paths
import logging 

logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s:%(levelname)s]:%(message)s"
                    )

while True:
    project_name = input("Enter the project name:")
    if project_name != '':
        break
                    
logging.info(f"Creating project by name:{project_name}")

#list of files:
list_of_files = [
        ".github/workflows/.gitkeep",  # action files,gitkeep is dummyfile to keep workflows dir
        f"src/{project_name}/__init__.py", # this tell this is a project file
        f"tests/__init__.py",
        f"tests/unit/__init__.py", # these two tests folders for creating robust package
        f"tests/integration/__init__.py",
        "init_setup.sh", # help to create repo for env setup
        "requirements.txt",
        "requirements_dev.txt", # this for libraries for testing 
        "setup.py",  # to install all packages
        "pyproject.toml", # 
        "setup.cfg",
        "tox.inl"  #python packages need to be tested on various environments this will help for that

]

for filepath in list_of_files:
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a directory at: {filedir} for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating a new file: {filename} at path: {filepath}")
    else:
        logging.info(f"file is already present at: {filepath}")
