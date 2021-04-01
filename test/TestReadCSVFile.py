import unittest, csv
from unittest import mock
from unittest.mock import MagicMock
from src.DataSource.ReadCSVFile import ReadCSVFile
from src.DataSource.DataSourceConstants import *

class TestReadCSVFile(unittest.TestCase):

    readCSVFile = ReadCSVFile()

    def test_getCustomerDataFromFile(self):
        fileData = self.readCSVFile.getConfig(entitiesFolder,"customer" + ".csv")
        self.assertEqual( fileData[0] ,['derek.somerville@glasgow.ac.uk', 'Derek', 'Somerville', '1234'])

    def test_getLastLinesFromFile(self):
        fileLines = self.readCSVFile.getLastLines( entitiesFolder, "customer" + ".csv",1)
        self.assertEqual( fileLines ,['matthew.barr@glasgow.ac.uk', 'Matt', 'Barr', 'password'])

    #Mocks

    def test_readFileData(self):

        self.readCSVFile.getConfig = MagicMock(return_value=[['derek.somerville@glasgow.ac.uk', 'Derek', 'Somerville', '1234'],['matthew.barr@glasgow.ac.uk', 'Matt', 'Barr', '4321']])
        self.assertEqual(self.readCSVFile.getLastLines(entitiesFolder,"customer" + ".csv", 1) ,['matthew.barr@glasgow.ac.uk', 'Matt', 'Barr', '4321'])

    def test_readFileDataDerek(self):

        self.readCSVFile.getConfig = MagicMock(return_value=[['derek.somerville@glasgow.ac.uk', 'Derek', 'Somerville', '1234']])
        self.assertEqual(self.readCSVFile.getLastLines(entitiesFolder,"customer" + ".csv", 1) ,['derek.somerville@glasgow.ac.uk', 'Derek', 'Somerville', '1234'])

    def test_readFileDataReal(self):

        readCSVFile = ReadCSVFile()
        self.assertEqual(readCSVFile.getLastLines(entitiesFolder,"customer" + ".csv", 1) ,['matthew.barr@glasgow.ac.uk', 'Matt', 'Barr', 'password'])


def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()

