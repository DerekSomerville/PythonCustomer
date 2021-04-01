import unittest
from src.Display.TestInput import TestInput
from src.Entities.CustomerOrder import CustomerOrder
from src.Display.InputConsole import InputConsole
from src.DataSource.ReadCSVFile import ReadCSVFile

class UserInputTest(unittest.TestCase):


    def fakeInput(self):


        fakeUserTestInput = TestInput()
        fakeUserTestInput.setInputList([1,2,3,4,5,6])

        fakeCustomerOrder = CustomerOrder(fakeUserTestInput)

        return fakeCustomerOrder

    def test_FakeInput(self):

        fakeInputTest = self.fakeInput()
        fakeOrderedItems = fakeInputTest.addItem()
        self.assertEqual(fakeOrderedItems[0], ['Orange Mango and Passion Fruit', '5.00'])


if __name__ == '__main__':
    unittest.main()
