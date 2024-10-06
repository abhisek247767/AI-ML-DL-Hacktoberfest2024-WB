import os
import sys
from six.moves import urllib
import zipfile
from isd.logger import logging
from isd.exception import isdException
from isd.entity.config_entity import DataIngestionConfig
from isd.entity.artifacts_entity import DataIngestionArtifact
from isd.configuration.s3_operations import S3Operation
from isd.constant.training_pipeline import *


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
            self.s3 = S3Operation()
        except Exception as e:
           raise isdException(e, sys)


    def download_data(self)-> str:
        '''
        Fetch data from s3
        '''
        try: 
            zip_download_dir = self.data_ingestion_config.data_ingestion_dir
            os.makedirs(zip_download_dir, exist_ok=True)
            logging.info(f"Downloading data from s3 into file {zip_download_dir}")
            zip_file_path = os.path.join(zip_download_dir, self.data_ingestion_config.S3_DATA_NAME)
            self.s3.download_object(key= self.data_ingestion_config.S3_DATA_NAME, bucket_name=DATA_BUCKET_NAME, filename = zip_file_path)
            logging.info(f"Downloaded data from s3 into file {zip_file_path}")
            return zip_file_path

        except Exception as e:
            raise isdException(e, sys)

    
    def extract_zip_file(self,zip_file_path: str)-> str:
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        try:
            feature_store_path = self.data_ingestion_config.feature_store_file_path
            os.system(f"unzip {zip_file_path} -d {feature_store_path}")
            
            return feature_store_path

        except Exception as e:
            raise isdException(e, sys)


    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        logging.info("Entered initiate_data_ingestion method of Data_Ingestion class")
        try: 
            zip_file_path = self.download_data()
            feature_store_path = self.extract_zip_file(zip_file_path)

            data_ingestion_artifact = DataIngestionArtifact(
                data_zip_file_path = zip_file_path,
                feature_store_path = feature_store_path
            )
            logging.info("Exited initiate_data_ingestion method of Data_Ingestion class")
            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")

            return data_ingestion_artifact

        except Exception as e:
            raise isdException(e, sys)
        