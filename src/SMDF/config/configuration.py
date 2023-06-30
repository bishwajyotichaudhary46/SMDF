from SMDF.constants import *
from SMDF.utils.common import read_yaml,create_directories
from SMDF.entity import (ModelTrainerConfig,DataSplitingConfig,DataIngestionConfig,DataValidationConfig,DataTransformationConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH
        ):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        

        create_directories([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )

        return data_transformation_config
    
    def get_data_spliting_config(self) -> DataSplitingConfig:
        config = self.config.data_spliting

        create_directories([config.root_dir])

        data_spliting_config = DataSplitingConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )

        return data_spliting_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.hybrid
        schema = self.schema.trainer_column

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            filters = params.filters,
            kernel_size = params.kernel_size,
            scaler = config.scaler,
            activation = params.activation,
            loss = params.loss,
            optimizer = params.optimizer,
            epoch=params.epoch,
            batch_size=params.batch_size,
            M01AB = config.M01AB,
            M01AE = config.M01AE,
            N02BA = config.N02BA,
            N02BE = config.N02BE,
            N05B = config.N05B,
            N05C = config.N05C,
            R03 = config.R03,
            R06 = config.R06,
            

            
        )

        return model_trainer_config
