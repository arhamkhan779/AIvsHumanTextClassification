from AIvsHumanTextClassification import logger
from AIvsHumanTextClassification.pipeline.DATA_INGESTION_PIPELINE import DataIngestionPipeline
from AIvsHumanTextClassification.pipeline.DATA_CLEANING_PIPELINE import DataCleaningPipeline
from AIvsHumanTextClassification.pipeline.DATA_PREPROCESSING_PIPELINE import DataProcessingPipeline
from AIvsHumanTextClassification.pipeline.PREPARE_BASE_MODEL_PIPELINE import PrepareBaseModelPipeline
from AIvsHumanTextClassification.pipeline.MODEL_TRAINER_PIPELINE import ModelTrainingPipeline


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

STAGE_NAME="DATA PRPROCESSING STAGE"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started >>>>>>")
    obj=DataProcessingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed >>>>>>")

except Exception as e:
    logger.info(e)
    raise e


STAGE_NAME="PREPARE BASE MODEL "

try:
    logger.info(f">>>>> stage {STAGE_NAME} started >>>>>>")
    obj=PrepareBaseModelPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed >>>>>>")
except Exception as e:
    raise e

STAGE_NAME="MODEL TRAINING STAGE "

try:
    logger.info(f">>>>> stage {STAGE_NAME} started >>>>>>")
    obj=ModelTrainingPipeline()
    obj.main(plots=True)
    logger.info(f">>>>> stage {STAGE_NAME} completed >>>>>>")
except Exception as e:
    raise e