import unittest, csv
from unittest import mock
from unittest.mock import MagicMock
from src.DataSource.ReadCSVFile import ReadCSVFile
from src.DataSource.DataSourceConstants import *

class TestReadCSVFile(unittest.TestCase):

    readCSVFile = ReadCSVFile()

    def test_getCustomerDataFromFile(self):
        fileData = self.readCSVFile.getFileData(ENTITIES_FOLDER,"customer" + ".csv")
        self.assertEqual( fileData[1] ,['derek.somerville@glasgow.ac.uk', 'Derek', 'Somerville', '1234'])

    def test_getLastLinesFromFile(self):
        fileLines = self.readCSVFile.getLastLines( ENTITIES_FOLDER, "customer" + ".csv",1)
        self.assertEqual( fileLines ,['matthew.barr@glasgow.ac.uk', 'Matt', 'Barr', '4321'])

def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()

