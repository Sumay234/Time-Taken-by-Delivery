from dataclasses import dataclass


# Here we call all our training & testing file data
class DataIngestionArtifact:
    feature_store_file_path:str
    train_file_path:str
    test_file_path:str
    
    
    