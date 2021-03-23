from src.Display.ReadSmoothieFile import Menu

class CustomerOrder:
    def __init__(self, orderedItems=[]):
        self.orderedSmoothies = orderedItems

    def placeOrder(self):
        orderNumber = int(input())
        smoothieMenu = Menu.SmoothieMenu(self)
        while True:
            for item in smoothieMenu:
                if item[0][0] == str(orderNumber):
                    self.orderedSmoothies.append(item[1])
                    elem = self.orderedSmoothies.pop()
                    self.orderedSmoothies.append(elem)
                    print("You have added", elem)
            print("Do you want to order anything else, 1 for yes, 2 for no")
            continueOrdering = int(input())
            if continueOrdering == 1:
                print("Pick another number to order")
                return self.placeOrder()
            elif continueOrdering >= 2 or continueOrdering < 1:
                return "You have ordered:\n " + str(self.orderedSmoothies).replace("[", "").replace("]", ""). \
                    replace("(", "").replace(")", "").replace(",", "\n").replace("'", "") + " Smoothie"