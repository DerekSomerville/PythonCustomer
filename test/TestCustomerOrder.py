import unittest
from src.Entities.CustomerOrder import CustomerOrder



class Test_AddItemOrder(unittest.TestCase):
    def testAddItem(self):
        customerOrder = CustomerOrder()



if __name__ == '__main__':
    unittest.main()
