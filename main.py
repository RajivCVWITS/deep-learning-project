from src.deep_learning_project import logger
from src.deep_learning_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>> Starting {STAGE_NAME} <<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> Completed {STAGE_NAME} <<<<\n\nx========x")

except Exception as e:
    logger.exception(e)
    raise e
