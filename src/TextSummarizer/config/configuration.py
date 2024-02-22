# importing constants => paths of config.yaml and params.yaml files
from TextSummarizer.constants import *
# importing utility functions from utils folder, common.py file
from TextSummarizer.utils.common import read_yaml, create_directories

from TextSummarizer.entity import (DataIngestionConfig,
                                   DataValidationConfig,
                                   DataTransformationConfig,
                                   ModelTrainerConfig,
                                   ModelEvaluationConfig)

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
    
    # config manager for data ingestion
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
    
    # config manager for data validation
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES,
        )

        return data_validation_config

    # config manager for data transformation
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name = config.tokenizer_name
        )

        return data_transformation_config
    
    # config manager for model trainer
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.TrainingArguments

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_ckpt = config.model_ckpt,
            num_train_epochs = params.num_train_epochs,
            warmup_steps = params.warmup_steps,
            per_device_train_batch_size = params.per_device_train_batch_size,
            weight_decay = params.weight_decay,
            logging_steps = params.logging_steps,
            evaluation_strategy = params.evaluation_strategy,
            eval_steps = params.eval_steps,
            save_steps = params.save_steps,
            gradient_accumulation_steps = params.gradient_accumulation_steps
        )

        return model_trainer_config

    # config manager for model evaluation
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_path = config.model_path,
            tokenizer_path = config.tokenizer_path,
            metric_file_name = config.metric_file_name
           
        )

        return model_evaluation_config
