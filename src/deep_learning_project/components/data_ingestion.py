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
        # Instead of downloading, just ensure the folder exists
        os.makedirs(self.config.unzip_dir, exist_ok=True)
        # You can add logging here if needed
        print(f"Using local data folder: {self.config.unzip_dir}")