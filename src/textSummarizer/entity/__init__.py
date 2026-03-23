from dataclasses import dataclass #dataclass: A decorator from the dataclasses module that automatically adds special methods to classes like __init__(), __repr__(), etc.
from pathlib import Path #Comes from the pathlib module. It provides an object-oriented interface to work with file system paths.

@dataclass(frozen=True)
class DataIngestionConfig: #This defines a class to hold configuration settings for the data ingestion step of a machine learning pipeline.
    #Attributes of the Class

    root_dir: Path#The root directory where all data-related operations will be handled.
    source_URL: str#The URL from where the raw data will be downloaded.
    local_data_file: Path#The local file path where the downloaded data will be stored
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir:Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file_name: Path
