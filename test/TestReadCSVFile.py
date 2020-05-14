import unittest, csv
from unittest import mock
from unittest.mock import MagicMock
from src.ReadCSVFile import ReadCSVFile

class TestReadCSVFile(unittest.TestCase):

    def test_getCustomerDataFromFile(self):
        readCSVFile = ReadCSVFile()
        fileData = readCSVFile.getFileData("Entities/","customer" + ".csv")
        self.assertEqual( fileData[1] ,['derek.somerville@glasgow.ac.uk', 'Derek', 'Somerville', '1234'])

def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()

