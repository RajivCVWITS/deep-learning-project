from src.deep_learning_project.config.configuration import ConfigurationManager
from src.deep_learning_project.components.data_ingestion import DataIngestion
from src.deep_learning_project import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()

if __name__ == "__main__":
    try:
        logger.info(f">>>> Starting {STAGE_NAME} <<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>> Completed {STAGE_NAME} <<<<\n\nx========x")

    except Exception as e:
        logger.exception(e)
        raise e