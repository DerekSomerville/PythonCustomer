import unittest
from src.Entities.CustomerFunds import CustomerFunds

class Test_CustomerFunds(unittest.TestCase):


    def test_customerFunds(self):
        customerFunds = CustomerFunds()
        customerFunds.getFunds()
        payout = customerFunds.payOrder(50000)
        self.assertEqual(payout, "You don't have enough funds to purchase these items.")

if __name__ == '__main__':
    unittest.main()