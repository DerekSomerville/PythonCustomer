from Output import Output
from WriteToFile import WriteToFile

class OutputConsole(Output):

    writeToFile = True
    outputWriteToFile = WriteToFile("userOutputLog.csv")

    def print(self, output):
        if self.writeToFile:
            self.outputWriteToFile.writeToFile(output)
        print(output)

def main():
    outputConsole = OutputConsole()
    outputConsole.print("Hello World")

if __name__ == "__main__":
    main()
