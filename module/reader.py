import glob
import json
import pandas as pd
import os
import exceptions
import traceback
import logging.config
from dotenv import load_dotenv
from config.settings import dotenv_path


logging.config.fileConfig("common/log_conf.ini",disable_existing_loggers=False)
_fileHandler_logger=logging.getLogger('%s.%s' % (__name__, 'FileHandler'))

load_dotenv(dotenv_path)
from config import settings


class FileHandler:
    def __init__(self):
        self.files_path = settings.data_path
        self.data = []
        self.data_processed = None

    def extract(self,file_name=None):
        """ Read all files from ata path directory and save to FileHandler data property """
        if file_name is None:
            files = glob.iglob(os.path.join(self.files_path,'**/*.json'), recursive=True)
        else:
            files = file_name
        for file in files:
        #for file in glob.iglob(os.path.join(self.files_path,'**/*.json'), recursive=False):
            try:
                with open(file) as inputData:
                    _fileHandler_logger.info("%s %s","Extract a data from files",file)
                    for line in inputData:
                        self.data.append(json.loads(line.rstrip('\n')))

            except Exception as err:
                _fileHandler_logger.error(err, exc_info=False)
                raise exceptions.FileReaderError(
                    'Please check if the file "%s" is already in the folder \n '
                    'Error in detail: \n %s' % (file, err.__str__())) from None
            except:
                _fileHandler_logger.error("uncaught exception: %s", traceback.format_exc())
                return False

    def transform(self):
        """ Process data extracted and save to the data_processed property of FileHandler """

        df_normalized = pd.json_normalize(self.data, max_level=1)
        df_normalized['time'] = pd.to_datetime(df_normalized['time'])
        df_normalized['date'] = pd.to_datetime(df_normalized['time']).dt.to_period('D')
        df_normalized['year'] = pd.to_datetime(df_normalized['time']).dt.year
        df_normalized['hour'] = pd.to_datetime(df_normalized['time']).dt.hour
        df_normalized['month_year'] = pd.to_datetime(df_normalized['time']).dt.to_period('M')
        df_normalized['weekday'] = pd.to_datetime(df_normalized['time']).dt.dayofweek
        df_normalized['weekday_name'] = pd.to_datetime(df_normalized['time']).dt.day_name()

        self.data_processed = df_normalized

        return df_normalized
