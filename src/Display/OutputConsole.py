from src.Display.Output import Output
from src.DataSource.WriteToFile import WriteToFile
from src.DataSource.DataSourceConstants import *

class OutputConsole(Output):

    writeToFile = True
    outputWriteToFile = WriteToFile(userActionFolder,outputLog)

    def print(self, message):
        if self.writeToFile:
            self.outputWriteToFile.writeToFile(message)
        print(message)

def main():
    outputConsole = OutputConsole()
    outputConsole.print("Hello World:)")

if __name__ == "__main__":
    main()
