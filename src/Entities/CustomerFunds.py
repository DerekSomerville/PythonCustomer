from src.Display.InputConsole import InputConsole
from src.Entities.CustomerOrder import CustomerOrder

class CustomerFunds:
    def __init__(self):
        self.wallet = InputConsole()
        self.userFunds = ""
        self.userPayment = ""

    def getFunds(self):
        self.userFunds = self.wallet.getInputInt("Enter the amount of funds you have available: \n")
        return "Your current funds are: " + "£" + str(self.userFunds)

    def payOrder(self, orderTotal):
        self.userPayment = int(self.userFunds) - orderTotal
        if self.userPayment < 0:
            return "You don't have enough funds to purchase these items."
        else:
            self.userFunds = self.userPayment
            return "Your remaining funds are: " + "£" + str(self.userFunds)



