import unittest
from src.DataSource.ReadCSVFile import ReadCSVFile
from src.Display.OutputConsole import OutputConsole
from src.DataSource.DataSourceConstants import *

class TestOutputConsole(unittest.TestCase):

    output_console = OutputConsole()
    read_csc_file = ReadCSVFile()

    def test_print(self):
        self.output_console.print("A test of output_console.print")
        output_line = self.read_csc_file.get_last_lines(USERACTION_FOLDER,OUTPUT_LOG,1)
        self.assertEqual(["A test of output_console.print"], output_line)

def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()
