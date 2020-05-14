import unittest
from unittest import mock
from unittest.mock import MagicMock
from src.DataSource.ReadCSVFile import ReadCSVFile
from src.EntitiesDatabaseMapping.CustomerDatabaseMapping import CustomerDatabaseMapping

class TestCustomerDatabaseMapping(unittest.TestCase):

    def test_getCustomerDataFromFile(self):
        readCSVFile = ReadCSVFile()
        customerDatabaseMapping = CustomerDatabaseMapping()
        customerData = customerDatabaseMapping.getCustomerDataFromFile()
        self.assertEqual( customerData[0] ,['derek.somerville@glasgow.ac.uk', 'Derek', 'Somerville', '1234'])

    def test_getCustomerDataFromDatabase(self):
        customerDatabaseMapping = CustomerDatabaseMapping()
        customerData = customerDatabaseMapping.getCustomerData()
        self.assertEqual( customerData[0] ,('derek.somerville@glasgow.ac.uk', 'Derek', 'Somerville', '1234'))

def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()
