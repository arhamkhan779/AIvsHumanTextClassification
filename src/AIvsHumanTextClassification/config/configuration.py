import os
from pathlib import Path
from AIvsHumanTextClassification.constants import *
from AIvsHumanTextClassification.utils.common import read_yaml,create_directories
from AIvsHumanTextClassification.entity.config_entity import DataIngstionConfig,DataCleaningConfig

class ConfigurationManager:
    def __init__(self,
                 config_file_path=CONFIG_FILE_PATH,
                 params_file_path=PARAMS_FILE_PATH):
        
        self.config=read_yaml(config_file_path)
        self.params=read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngstionConfig:
        config=self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config=DataIngstionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
    def get_data_cleaning_config(self) -> DataCleaningConfig:
        config=self.config.data_clean
        create_directories([config.root_dir])

        data_cleaning_config=DataCleaningConfig(
            root_dir=config.root_dir,
            source_dir=config.source_dir,
            fina_dir=config.final_dir
        )
        return data_cleaning_config
