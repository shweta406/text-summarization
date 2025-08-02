from dataclasses import dataclass #dataclass: A decorator from the dataclasses module that automatically adds special methods to classes like __init__(), __repr__(), etc.
from pathlib import Path #Comes from the pathlib module. It provides an object-oriented interface to work with file system paths.

@dataclass(frozen=True)
class DataIngestionConfig: #This defines a class to hold configuration settings for the data ingestion step of a machine learning pipeline.
    #Attributes of the Class

    root_dir: Path#The root directory where all data-related operations will be handled.
    source_URL: str#The URL from where the raw data will be downloaded.
    local_data_file: Path#The local file path where the downloaded data will be stored
    unzip_dir: Path