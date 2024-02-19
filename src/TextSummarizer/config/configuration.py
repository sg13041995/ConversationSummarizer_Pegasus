# importing constants => paths of config.yaml and params.yaml files
from TextSummarizer.constants import *
# importing utility functions from utils folder, common.py file
from TextSummarizer.utils.common import read_yaml, create_directories

from TextSummarizer.entity import (DataIngestionConfig)

class ConfigurationManager:
    # constructor
    def __init__(
        self,
        # paths to yaml files for reading their content
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH
        ):
        
        # reading content from both the yaml files
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # creating root artifacts folder
        # from config.yaml => getting artifacts_root value
        # self.config.artifacts_root is same as => self.config["artifacts_root"] 
        create_directories([self.config.artifacts_root])
    
    # method for data_ingestion 
    # return datatype is DataIngestionConfig
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        # reading => data_ingestion config
        config = self.config.data_ingestion

        # creating directory using config.root_dir => artifacts/data_ingestion
        create_directories([config.root_dir])

        # constructing return details related to the data_ingestion from => config.yaml data_ingestion section
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config