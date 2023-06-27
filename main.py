from SMDF.pipeline.stage_01_dataingestion import DataIngestionTrainingPipeline
from SMDF.logging import logger


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} sucessfully completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
