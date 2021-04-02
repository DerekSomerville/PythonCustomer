import unittest
from src.Entities.CustomSmoothie import CustomSmoothie
from src.Display.ReadSmoothieFile import ReadSmoothieFile
from src.Display.TestInput import TestInput
from src.Display.InputConsole import InputConsole


class TestCustomSmoothie(unittest.TestCase):

    def fakeOrderInput(self):
        # Creates a smoothie with 3 ingredients

        fakeUserTestInput = TestInput()
        fakeUserTestInput.setInputList([1, 1, 1, 2, 1, 3, 4])

        fakeCustomSmoothie = CustomSmoothie(fakeUserTestInput)

        return fakeCustomSmoothie

    def fakeOrderInputWithRemoveIngredient(self):
        #Creates a smoothie with 3 ingredients then removes the 3rd ingredient

        fakeUserTestInput = TestInput()

        # 2, 2, 9 calls removeIngredient method, selects last ingredient (Fennel) for removal,
        # and finalises the amended custom smootie
        fakeUserTestInput.setInputList([1, 1, 1, 2, 1, 3, 2, 2, 9])

        fakeCustomSmoothie = CustomSmoothie(fakeUserTestInput)

        return fakeCustomSmoothie

    def test_OrderIngredient(self):
        fakeCustomSmoothie = self.fakeOrderInput()
        fakeOrderedIngredients = fakeCustomSmoothie.createCustomSmoothie()
        self.assertEqual(fakeOrderedIngredients, 'Custom smoothie: Banana, Mango, Fennel')

    def test_RemoveIngredient(self):
        fakeCustomSmoothie = self.fakeOrderInputWithRemoveIngredient()
        fakeOrderedIngredients = fakeCustomSmoothie.createCustomSmoothie()
        self.assertEqual(fakeOrderedIngredients, 'Custom smoothie: Banana, Mango')


if __name__ == '__main__':
    unittest.main()
