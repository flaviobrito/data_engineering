
"""
Tasks:
- define exception classes [OK]
- define log config [OK]
- define environment variables [OK]
- define settings values - [OK]
- implement a function that reads data  [OK]
- implement a function that process data objects [OK]
- implement a function that export  data to other type of data [OK]
- implement  data test [OK]

"""

"""
# Imports
"""
import pandas as pd
import logging
from logging import config
from dotenv import load_dotenv
from config.settings import dotenv_path

"""
# Local Import 
"""
from config.settings import  data_path,image_path
from module.reader import FileHandler
from module.analysis import AnalysisHandler
from db.database import DBHandler
"""
#Variables and configurations
"""
logging.config.fileConfig("common/log_conf.ini",disable_existing_loggers=False)
_logger  = logging.getLogger(__name__)
pd.set_option('display.max_columns', None)
load_dotenv(dotenv_path)

"""Instances"""
file  =  FileHandler()
db = DBHandler()
_logger.info("############################ EXTRACT DATA ##############################")

file.extract()

_logger.info("############################ TRANSFORM DATA ##############################")

data_processed = file.transform()

#logging.info("%s %s", "Data",file.data_processed.head())

_logger.info("############################ ANALYSIS DATA ##############################")

"""Instances"""

analyze = AnalysisHandler()
analyze.data_processed = data_processed
results = analyze.analysis(data_processed)

_logger.info("############################ ********* ##############################")
logging.info("%s %s", "Stats",analyze.stats)
logging.info("%s %s", "Missing",analyze.missings)
logging.info("%s %s", "Access per Host",analyze.access_per_host)
logging.info("%s %s", "Number of unique visitors",analyze.unique_visitors)
logging.info("%s %s", "Number of Visits per User",analyze.visits_per_user)
logging.info("%s %s", "Number of Visits per Year - Hour",analyze.visits_per_year_hour)

_logger.info("############################  SAVE DATA - DATABASE ##############################")

logging.info("Saving Stats data into Database")
db.save(analyze.stats,'stats')
logging.info("Saving Missing data into Database")
db.save(analyze.missings,'missings')
logging.info("Saving Access per Host data into Database")
db.save(analyze.access_per_host,'access_per_host')
logging.info("Saving Unique Visitors data into Database")
db.save(analyze.unique_visitors,'unique_visitors')
logging.info("Saving Visists per USer data into Database")
db.save(analyze.visits_per_user,'visits_per_user')
logging.info("Saving Visists per Year / Hour data into Database")
db.save(analyze.visits_per_year_hour,'visits_per_year_hour')
logging.info("Saving Processed data into Database")
db.save(analyze.data_processed,'data_processed')