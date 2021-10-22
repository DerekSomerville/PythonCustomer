from abc import ABC, abstractmethod

class Input(ABC):

    @abstractmethod
    def get_input_string(self, request):
        pass

    def get_input_int(self, request):
        response = self.get_input_string(request)
        while not str(response).isnumeric():
            response = self.get_input_string("Please enter an integer")
        return int(response)



