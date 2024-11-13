from AIvsHumanTextClassification.config.configuration import ConfigurationManager
from AIvsHumanTextClassification.components.Data_Ingeston import DataIngestion
from AIvsHumanTextClassification import logger

STAGE_NAME="DATA INGESTION STAGE"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()