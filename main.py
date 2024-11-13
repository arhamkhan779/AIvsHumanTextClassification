from AIvsHumanTextClassification import logger
from AIvsHumanTextClassification.pipeline.DATA_INGESTION_PIPELINE import DataIngestionPipeline
from AIvsHumanTextClassification.pipeline.DATA_CLEANING_PIPELINE import DataCleaningPipeline


STAGE_NAME="DATA INGESTION STAGE"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started >>>>>>")
    obj=DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed >>>>>>")

except Exception as e:
    logger.info(e)
    raise e

STAGE_NAME="DATA ClEANING STAGE"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started >>>>>>")
    obj=DataCleaningPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed >>>>>>")

except Exception as e:
    logger.info(e)
    raise e