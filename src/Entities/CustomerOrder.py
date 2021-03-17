class CustomerOrder:

    def addItems(self):
        order = []
        ordernumber = 99
        while ordernumber != 0:
            ordernumber = int(input("Please input the number of the item you want. Input 0 to finish: "))
            if ordernumber == 1:
                order.append("Strawberry")
            elif ordernumber == 2:
                order.append("Vanilla")
            elif ordernumber == 3:
                order.append("Chocolate")
            elif ordernumber == 4:
                order.append("Mint")
            elif ordernumber == 5:
                order.append("Banana")
            print(order)
        return order
