from deep_learning_project.constants import *
from deep_learning_project.utils.common import read_yaml, create_directories
from deep_learning_project.entity.config_entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(
        self,
        config_file_path = CONFIG_FILE_PATH,
        params_file_path = PARAMS_FILE_PATH):

        print("Config path:", config_file_path)
        print("Params path:", params_file_path)

        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

        print("Config loaded:", self.config)     # Debug print
        print("Params loaded:", self.params)     # Debug print


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        get_data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )

        return get_data_ingestion_config



