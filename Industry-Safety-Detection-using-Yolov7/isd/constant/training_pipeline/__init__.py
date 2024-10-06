ARTIFACTS_DIR: str = "artifacts"


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

DATA_INGESTION_S3_DATA_NAME: str = "isd_data_mini.zip"

DATA_BUCKET_NAME = "isd-data-24"


"""
Data Validation realted contant start with DATA_VALIDATION VAR NAME
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_STATUS_FILE = 'status.txt'

DATA_VALIDATION_ALL_REQUIRED_FILES = ["images", "labels", "classes.names", "train.txt", "val.txt"]


"""
MODEL TRAINER related constant start with MODEL_TRAINER var name
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"

MODEL_TRAINER_PRETRAINED_WEIGHT_URL: str = "https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt"

MODEL_TRAINER_NO_EPOCHS: int = 1

MODEL_TRAINER_BATCH_SIZE: int = 8


"""
MODEL PUSHER related constant start with MODEL_PUSHER var name
"""
MODEL_BUCKET_NAME = "isd-data-24"
S3_MODEL_NAME = "best.pt"