# data ingestion pipeline class
from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
# data validation pipeline class
from TextSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
# data transformation pipeline class
from TextSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline

# textSummarizer we have installed as local package
# importing logger from logging.py
from TextSummarizer.logging import logger

# data ingestion
STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   # main method => triggers the pipeline
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

# data validation
STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   # main method => triggers the pipeline
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

# data transformation
STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_transformation = DataTransformationTrainingPipeline()
   # main method => triggers the pipeline
   data_transformation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
