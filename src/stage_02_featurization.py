import argparse
import os
import shutil
from tqdm import tqdm
import logging
from src.utils.common import read_yaml,create_dirs


STAGE = 'Two'
logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )

def main(config_path, params_path):
    ## converting XML data tsv
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    #source_data = config['source_data']
    artifacts = config['artifacts']
    artifacts_dir = artifacts['ARTIFACTS_DIR']
    prepared_data_dir_path = os.path.join(artifacts_dir, artifacts["PREPARED_DATA"])
    train_data_path = os.path.join(prepared_data_dir_path, artifacts['TRAIN_DATA'])
    test_data_path = os.path.join(prepared_data_dir_path, artifacts['TEST_DATA'])

    featurized_data_dir_path = os.path.join(artifacts_dir, artifacts['FEATURIZED_DATA'])
    create_dirs([featurized_data_dir_path])
    featurized_train_data = os.path.join(featurized_data_dir_path, artifacts['FEATURIZED_OUT_TRAIN'])
    featurized_test_data = os.path.join(featurized_data_dir_path, artifacts['FEATURIZED_OUT_TEST'])





if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")

    parsed_args = args.parse_args()

    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main(config_path=parsed_args.config, params_path=parsed_args.params)
        logging.info(f">>>>> stage {STAGE} completed! <<<<</n")
    except Exception as e:
        logging.exception(e)
        raise e