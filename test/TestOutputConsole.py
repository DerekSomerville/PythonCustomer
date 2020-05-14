import unittest
from src.DataSource.ReadCSVFile import ReadCSVFile
from src.Display.OutputConsole import OutputConsole
from src.DataSource.DataSourceConstants import *

class TestOutputConsole(unittest.TestCase):

    outputConsole = OutputConsole()
    readCSCFile = ReadCSVFile()

    def testPrint(self):
        self.outputConsole.print("A test of outputConsole.print")
        outputLine = self.readCSCFile.getLastLines(USERACTION_FOLDER,OUTPUT_LOG,1)
        self.assertEqual(["A test of outputConsole.print"], outputLine)

def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()
