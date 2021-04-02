import unittest
from unittest import mock
from unittest.mock import MagicMock
from src.Entities.CustomerOrder import CustomerOrder


class TestCustomerOrder(unittest.TestCase):
    def test_addItems(self):
        testCustomerOrder = CustomerOrder()
        order = testCustomerOrder.addItem()
        self.assertEqual(order[0], ['Orange Mango and Passion Fruit', '5.00'])

        return order

    def test_orderReview(self):
        testCustomerOrder = CustomerOrder()
        order = self.test_addItems()
        orderReview = testCustomerOrder.orderReview(order)
        print(orderReview)

        self.assertEqual(orderReview[0:37], '\nOrange Mango and Passion Fruit £5.00')

    def test_orderTotal(self):
        testCustomerOrder = CustomerOrder()
        testCustomerOrder.orderTotal = MagicMock(return_value=20)
        self.assertEqual(testCustomerOrder.orderTotal(), 20)


if __name__ == '__main__':
    unittest.main()
