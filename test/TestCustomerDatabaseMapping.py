import unittest
from unittest import mock
from unittest.mock import MagicMock
from src.DataSource.ReadCSVFile import ReadCSVFile
from src.EntitiesDatabaseMapping.CustomerDatabaseMapping import CustomerDatabaseMapping

class TestCustomerDatabaseMapping(unittest.TestCase):

    def test_get_customer_data_from_file(self):
        read_csv_file = ReadCSVFile()
        customer_database_mapping = CustomerDatabaseMapping()
        customer_data = customer_database_mapping.get_customer_data_from_file()
        self.assertEqual( customer_data[0] ,['derek.somerville@glasgow.ac.uk', 'Derek', 'Somerville', '1234'])

    def test_get_customer_data_from_database(self):
        customer_database_mapping = CustomerDatabaseMapping()
        customer_data = customer_database_mapping.get_customer_data()
        self.assertEqual( customer_data[0] ,('derek.somerville@glasgow.ac.uk', 'Derek', 'Somerville', '1234'))

def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()
