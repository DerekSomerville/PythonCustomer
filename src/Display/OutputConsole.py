from src.Display.Output import Output
from src.DataSource.WriteToFile import WriteToFile
from src.DataSource.DataSourceConstants import *

class OutputConsole(Output):

    write_to_file = True
    output_write_to_file = WriteToFile(USERACTION_FOLDER,OUTPUT_LOG)

    def print(self, message):
        if self.write_to_file:
            self.output_write_to_file.write_to_file(message)
        print(message)

def main():
    output_console = OutputConsole()
    output_console.print("Hello World:)")

if __name__ == "__main__":
    main()
