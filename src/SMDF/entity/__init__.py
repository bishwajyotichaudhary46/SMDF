from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: str
    
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    sales_data: Path

@dataclass(frozen=True)
class DataSplitingConfig:
    root_dir: Path
    data_path: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    scaler: str
    filters: int
    kernel_size: int
    activation: str
    loss: str
    optimizer: str
    epoch: int
    batch_size: int
    M01AB: Path
    M01AE: Path
    N02BA: Path
    N02BE: Path
    N05B: Path
    N05C: Path
    R03: Path
    R06: Path




@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    M01AB: Path
    M01AE: Path
    N02BA: Path
    N02BE: Path
    N05B: Path
    N05C: Path
    R03: Path
    R06: Path
    scaler: Path
     