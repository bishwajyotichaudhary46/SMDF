from SMDF.pipeline.stage_01_dataingestion import DataIngestionTrainingPipeline
from SMDF.logging import logger
from SMDF.pipeline.stage_02_datavalidation import DataValidationTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} sucessfully completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        datavalidatin = DataValidationTrainingPipeline()
        datavalidatin.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e