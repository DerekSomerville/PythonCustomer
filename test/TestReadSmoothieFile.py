import unittest
from src.Display.ReadSmoothieFile import ReadSmoothieFile


class TestReadSmoothieFile(unittest.TestCase):
    def testSmoothieFile(self):
        readSmoothieFile = ReadSmoothieFile()
        self.assertEqual(readSmoothieFile.smoothieFile()[0], ["1","Orange Mango and Passion Fruit","5.00"])


if __name__ == '__main__':
    unittest.main()
