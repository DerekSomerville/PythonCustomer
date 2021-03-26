from src.Display.ReadSmoothieFile import ReadSmoothieFile
from src.Entities.CustomerOrder import CustomerOrder
import sys


def main():
    combine = ""
    menu = ReadSmoothieFile()
    customerMenu = menu.smoothieFile("Smoothies")

    for words in customerMenu:
        combine += "\n" + ", ".join(words)

    print('Please select a smoothie from our menu', combine)

    order = CustomerOrder()
    orderedSmoothies = order.addItem()
    print("\nYour order is:", order.orderReview(orderedSmoothies))

    if isinstance(orderedSmoothies, str):
        sys.exit()
    else:
        order.removeItem()


if __name__ == '__main__':
    main()
