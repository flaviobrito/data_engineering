import unittest
from config.settings import data_path
from module.reader import  FileHandler

class Tests(unittest.TestCase):
    """Unit test class"""

    ## Definitions
    _FILE_TEST_ =  data_path / 'sample.json'

    print('file', _FILE_TEST_)

    ## Instance

    file = FileHandler()

    file.files_path = data_path


    # Objects
    def test_extract(self):
        """Teste extract data from json file"""
        self.assertTrue(self.file.extract(self._FILE_TEST_), "Error trying to read JSON file")