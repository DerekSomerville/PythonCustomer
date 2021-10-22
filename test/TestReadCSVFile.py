import unittest, csv
from unittest import mock
from unittest.mock import MagicMock
from src.DataSource.ReadCSVFile import ReadCSVFile
from src.DataSource.DataSourceConstants import *

class TestReadCSVFile(unittest.TestCase):

    read_csv_file = ReadCSVFile()

    def test_get_customer_data_from_file(self):
        file_data = self.read_csv_file.get_file_data(ENTITIES_FOLDER,"customer" + ".csv")
        self.assertEqual( file_data[1] ,['derek.somerville@glasgow.ac.uk', 'Derek', 'Somerville', '1234'])

    def test_get_last_lines_from_file(self):
        file_lines = self.read_csv_file.get_last_lines( ENTITIES_FOLDER, "customer" + ".csv",1)
        self.assertEqual( file_lines ,['matthew.barr@glasgow.ac.uk', 'Matt', 'Barr', '4321'])

def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()

