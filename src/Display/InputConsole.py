from src.Display.Input import Input
from src.DataSource.WriteToFile import WriteToFile

class InputConsole(Input):

    writeToFile = True
    userInputWriteToFile = WriteToFile("userInputLog.csv")

    def getInputString(self, request):
        userInput = input(request)
        if self.writeToFile:
            self.userInputWriteToFile.writeToFile(userInput)
        return userInput
