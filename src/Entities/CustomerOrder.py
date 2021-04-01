import sys
from src.Display.InputConsole import InputConsole
from src.Display.ReadSmoothieFile import ReadSmoothieFile
from src.Entities.CustomSmoothie import CustomSmoothie


class CustomerOrder:
    input = None

    def __init__(self, input=None):
        self.orderedSmoothies = []
        self.smoothieMenu = ReadSmoothieFile.smoothieFile(self, "Smoothies")
        self.combineOrder = ""
        self.customerBill = []
        self.confirmingOrder = True
        self.removingItem = True

        if input is None:
            self.input = InputConsole()
        else:
            self.input = input

    def addItem(self):
        userChoice = self.input.getInputInt("Enter the smoothie number to add it to your order or 0 to cancel order\n")

        while userChoice != 0 and userChoice <= len(self.smoothieMenu):
            for item in self.smoothieMenu:
                if item[0] == str(userChoice):
                    self.orderedSmoothies.append(item[1:])
                    elem = self.orderedSmoothies.pop()
                    self.orderedSmoothies.append(elem)
                    print("You have added", elem)
            if str(userChoice) == "5":
                customSmoothie = CustomSmoothie()
                print(customSmoothie.createCustomSmoothie())

            userChoice = self.input.getInputInt(
                "Enter another number if you want to add more items to your order or enter 0 to finish: ")

        if len(self.orderedSmoothies) > 0:
            return self.orderedSmoothies
        else:
            return "You have selected no smoothies"

    def orderReview(self, order):
        if isinstance(order, str):
            return order
        else:
            for item in order:
                self.combineOrder += "\n" + " £".join(item[0:])
            return self.combineOrder

    def confirmOrder(self):
        while self.confirmingOrder:
            confirmOrRemove = input("\nEnter 1 to confirm order and pay or 2 to edit and remove items\n")
            try:
                confirmOrRemove = int(confirmOrRemove)
            except ValueError:
                continue

            if confirmOrRemove == 1:
                self.confirmingOrder = False
            elif confirmOrRemove == 2:
                for item in range(len(self.orderedSmoothies)):
                    print(item, self.orderedSmoothies[item])
                self.removeItem()
                self.confirmingOrder = False

    def removeItem(self):
        while self.removingItem:
            removedItem = input("\nSelect the number for item you'd like to remove\n")

            try:
                removedItem = int(removedItem)
                print("You have removed:", self.orderedSmoothies.pop(removedItem))
                print("Your order is now:", self.orderedSmoothies)
                self.confirmOrder()
                self.removingItem = False

            except ValueError:
                continue
            except IndexError:
                print("Invalid number")

    def orderTotal(self):
        if isinstance(self.orderedSmoothies, str):
            sys.exit()
        elif len(self.orderedSmoothies) > 0:
            for item in self.orderedSmoothies:
                item = float(item[1])
                self.customerBill.append(item)

            return int(sum(self.customerBill))