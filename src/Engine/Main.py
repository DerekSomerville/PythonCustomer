from src.Display.ReadSmoothieFile import ReadSmoothieFile
from src.Entities.CustomerOrder import CustomerOrder
from src.Entities.CustomerFunds import CustomerFunds
import sys


def main():
    # Customer Wallet
    customerFunds = CustomerFunds()
    print(customerFunds.getFunds())

    # Menu
    combine = ""
    menu = ReadSmoothieFile()
    customerMenu = menu.smoothieFile("Smoothies")

    for words in customerMenu:
        combine += "\n" + ", ".join(words)

    print('Please select a smoothie from our menu', combine)

    # Customer Order
    order = CustomerOrder()
    orderedSmoothies = order.addItem()
    print("\nYour order is:", order.orderReview(orderedSmoothies))

    if isinstance(orderedSmoothies, str):
        sys.exit()
    else:
        order.confirmOrder()

    # Order Total/Bill
    orderTotal = order.orderTotal()
    print("Your total for the order is:" + " £" + str(orderTotal))
    print(customerFunds.payOrder(orderTotal))


if __name__ == '__main__':
    main()
