from abc import ABC, abstractmethod

class Input(ABC):

    @abstractmethod
    def getInputString(self, request):
        pass

    def getInputInt(self, request):
        response = self.getInputString(request)
        while not str(response).isnumeric():
            response = self.getInputString("Please enter a number")
        return int(response)



