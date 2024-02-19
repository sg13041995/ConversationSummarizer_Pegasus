import os
# to download the zipped data file using the URL
import urllib.request as request
import zipfile
# custom logger module
from TextSummarizer.logging import logger
# custom utility function
from TextSummarizer.utils.common import get_size

from pathlib import Path
from TextSummarizer.entity import (DataIngestionConfig)

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
   
    # method to download the data using provided URL
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  

    # extracting the downloaded zip file
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        # getting unzip dir path
        unzip_path = self.config.unzip_dir
        # creating unzip dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)