import unittest
from unittest import mock
from unittest.mock import MagicMock
from src.DataSource.ReadCSVFile import ReadCSVFile
from src.DataSource.StubCSV import StubCSV
from src.EntitiesDatabaseMapping.CustomerDatabaseMapping import CustomerDatabaseMapping

class TestCustomerDatabaseMapping(unittest.TestCase):


    customerDatabaseMapping = CustomerDatabaseMapping()

    def test_getCustomerDataFromFile(self):
        customerData = self.customerDatabaseMapping.getCustomerDataFromFile()
        self.assertEqual( customerData[0] ,['derek.somerville@glasgow.ac.uk', 'Derek', 'Somerville', '1234'])

    # Stub
    def test_getCustomerDataFromStub(self):
        readCSVFile = StubCSV()
        self.customerDatabaseMapping.setCustomerFileReader(readCSVFile)
        customerData = self.customerDatabaseMapping.getCustomerDataFromFile()
        self.assertEqual( customerData[0] ,['derek.somerville@glasgow.ac.uk','Derek', 'Somerville', 'password'])


def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()
