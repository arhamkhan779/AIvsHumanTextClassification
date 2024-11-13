from AIvsHumanTextClassification.config.configuration import ConfigurationManager
from AIvsHumanTextClassification.components.Data_Cleaning import DataCleaning
from AIvsHumanTextClassification import logger


class DataCleaningPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_cleaning_config=config.get_data_cleaning_config()
        data_cleaning=DataCleaning(config=data_cleaning_config)
        data_cleaning.Clean_file()
        