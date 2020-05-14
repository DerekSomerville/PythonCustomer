from src.Display.Output import Output
from src.DataSource.WriteToFile import WriteToFile
from src.DataSource.DataSourceConstants import *

class OutputConsole(Output):

    writeToFile = True
    outputWriteToFile = WriteToFile(USERACTION_FOLDER,OUTPUT_LOG)

    def print(self, output):
        if self.writeToFile:
            self.outputWriteToFile.writeToFile(output)
        print(output)

def main():
    outputConsole = OutputConsole()
    outputConsole.print("Hello World:)")

if __name__ == "__main__":
    main()
