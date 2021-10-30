import logging
import yaml
import os

def read_yaml(path_to_yaml:str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    logging.info(f"yaml  file: {path_to_yaml} loaded successfully")
    return content


def create_dirs(dirs: list):

    for dir in dirs:
        os.makedirs(dir, exist_ok=True)
        logging.info(f"Directory is created at {dir}")