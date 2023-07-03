from SMDF.pipeline.stage_01_dataingestion import DataIngestionTrainingPipeline
from SMDF.logging import logger
from SMDF.pipeline.stage_02_datavalidation import DataValidationTrainingPipeline
from SMDF.pipeline.stage_03_datatransformation import DataTransformatinTrainingPipeline
from SMDF.pipeline.stage_04_dataspliting import DataSplitingTrainingPipeline
from SMDF.pipeline.stage_05_modeltraining import ModelTrainingPipeline
from SMDF.pipeline.stage_06_modelevaluation import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} sucessfully completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Validation stage"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        datavalidatin = DataValidationTrainingPipeline()
        datavalidatin.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   datatransformation = DataTransformatinTrainingPipeline()
   datatransformation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} sucessfully completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Spliting stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   dataspliting = DataSplitingTrainingPipeline()
   dataspliting.main()
   logger.info(f">>>>>> stage {STAGE_NAME} sucessfully completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Training stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   modeltrainer = ModelTrainingPipeline()
   modeltrainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} sucessfully completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Evaluation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   modeleval = ModelEvaluationPipeline()
   modeleval.main()
   logger.info(f">>>>>> stage {STAGE_NAME} sucessfully completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e