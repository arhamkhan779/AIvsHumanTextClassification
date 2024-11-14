import os
import zipfile
from AIvsHumanTextClassification import logger
from AIvsHumanTextClassification.entity.config_entity import DataCleaningConfig
import pandas as pd
from AIvsHumanTextClassification.config.configuration import ConfigurationManager

class DataCleaning:
    def __init__(self, config: DataCleaningConfig):
        self.config = config

    def Clean_file(self) -> str:
        '''
        Cleaning Dataset
        '''
        try:
            logger.info(f"Loading Data From {self.config.source_dir}--> Start")
            dataset_url = self.config.source_dir
            df=pd.read_csv(dataset_url)
            logger.info("Loading Data From Directory --> Completed")

            logger.info("Dropping All the Null values")
            df.dropna(inplace=True)

            logger.info("Transforming Generated Column --> Start")
            X=df[['text']]
            Y=df[['generated']]
            logger.info("Loading Data From Directory")
            Y=Y['generated'].apply(lambda x : int(x))
            df=pd.concat([X,Y], axis=1)
            logger.info("Transforming Genrated Column --> Completed")

            logger.info("Balancing Dataset --> Start")
            df_0=df[df.generated==0]
            df_1=df[df.generated==1]
            df_0_final=df_0.sample(df_1.shape[0])
            df=pd.concat([df_1,df_0_final],axis=0)
            logger.info("Balancing Dataset --> Completed")

            df_0=df[df.generated==0]
            df_1=df[df.generated==1]

            df_0=df_0.sample(15000)
            df_1=df_1.sample(15000)
            df=pd.concat([df_1,df_0],axis=0)
            
            df.to_csv(self.config.fina_dir,index=False)
            logger.info(f"Save Clean file at {self.config.fina_dir}")

        except Exception as e:
            logger.error(f"Error occurred while downloading the dataset: {str(e)}")
            raise e
        