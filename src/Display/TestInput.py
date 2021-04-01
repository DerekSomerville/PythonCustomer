from src.Display.Input import Input

class TestInput(Input):

    inputList = []

    def setInputList(self,inputList):
        self.inputList = inputList

    def getInputString(self, request):
        return self.inputList.pop(0)

