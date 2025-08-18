import os
import urllib.request as request
import zipfile
from src.deep_learning_project import logger
from src.deep_learning_project.utils.common import get_size
from src.deep_learning_project.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        # Ensure the folder exists, but do NOT clear or overwrite if it already has data
        os.makedirs(self.config.unzip_dir, exist_ok=True)
        if os.listdir(self.config.unzip_dir):
            logger.info(f"Data already present in {self.config.unzip_dir}, skipping download.")
        else:
            logger.info(f"No data found in {self.config.unzip_dir}. Please upload data manually or configure download.")