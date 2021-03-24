from src.Display.Input import Input
from src.DataSource.WriteToFile import WriteToFile
from src.DataSource.DataSourceConstants import *

class InputConsole(Input):

    writeToFile = True
    userInputWriteToFile = WriteToFile(userActionFolder,inputLog)

    def getInputString(self, request):
        userInput = input(request)
        if self.writeToFile:
            self.userInputWriteToFile.writeToFile(userInput)
        return userInput
