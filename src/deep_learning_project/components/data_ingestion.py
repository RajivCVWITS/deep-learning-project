import os
import urllib.request as request
import zipfile
from deep_learning_project import logger
from deep_learning_project.utils.common import get_size
from deep_learning_project.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
         # Ensure parent directory exists before downloading
        os.makedirs(os.path.dirname(self.config.local_data_file), exist_ok=True)
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL, 
                filename = self.config.local_data_file)
            logger.info(f"{filename} downloaded with following info: \n{headers}")

        else:
            logger.info(f"File already exists at {self.config.local_data_file}")

