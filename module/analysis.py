import pandas as pd
import os
import exceptions
import traceback
import logging.config
from dotenv import load_dotenv
from config.settings import dotenv_path
from module.reader import FileHandler


logging.config.fileConfig("common/log_conf.ini",disable_existing_loggers=False)
_analysisHandler_logger=logging.getLogger('%s.%s' % (__name__, 'Analysis'))

load_dotenv(dotenv_path)
from config import settings


class AnalysisHandler(FileHandler):
    def __init__(self):
        self.data_processed = FileHandler().data_processed
        self.stats = None
        self.missings = None
        self.access_per_host = None
        self.unique_visitors = None
        self.visits_per_user = None
        self.visits_per_year_hour = None

        super().__init__()

    def analysis(self, data):
        """ Add comments"""

        self.data_processed = data
        self.stats = pd.DataFrame(self.data_processed).describe()
        self.missings = pd.DataFrame(self.data_processed).isnull().sum().sort_values(ascending = False)
        self.access_per_host = pd.DataFrame(self.data_processed["host"].value_counts())
        self.unique_visitors = pd.DataFrame(self.data_processed["user_name"].unique())
        self.visits_per_user = pd.DataFrame(self.data_processed["user_name"].value_counts())
        self.visits_per_year_hour =pd.DataFrame(self.data_processed.groupby('year')['hour'].value_counts().sort_index().reset_index(name='Count'))

        return self.stats

