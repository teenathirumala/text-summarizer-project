import os
import urllib.request as request
import zipfile
from textSummerizer.logging import logger
from textSummerizer.utils.common import get_size
from pathlib import Path
from textSummerizer.entity import DataIngestionConfig



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config



    def download_file(self):
        """#+
        Downloads a file from a specified URL if it doesn't already exist locally.#+
#+
        This method checks if the file specified in self.config.local_data_file exists.#+
        If it doesn't, it downloads the file from self.config.source_URL and saves it#+
        to self.config.local_data_file. If the file already exists, it logs the file size.#+
#+
        Parameters:#+
        None#+
#+
        Returns:#+
        None#+
#+
        Side effects:#+
        - Creates a new file if it doesn't exist#+
        - Logs information about the download or existing file#+
        """#+
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")


        
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)