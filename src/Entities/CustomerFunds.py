from src.Display.InputConsole import InputConsole
from src.Entities.CustomerOrder import CustomerOrder

class CustomerFunds:
    def __init__(self):
        self.wallet = InputConsole()
        self.userFunds = ""

    def getFunds(self):
        self.userFunds = self.wallet.getInputInt("Enter the amount of funds you have available: \n")
        return "£" + str(self.userFunds)

    def payOrder(self):

        self.userFunds = self.userFunds - sum(CustomerOrder.customerBill)
        return "Your remaining funds are now: " + "£" + str(self.userFunds)




