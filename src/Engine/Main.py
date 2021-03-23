from src.Display.ReadSmoothieFile import Menu
from src.Entities.CustomerOrder import CustomerOrder


def main():
    combine = ""
    menu = Menu()
    customerMenu = menu.Smoothie_Menu()

    for words in customerMenu:
        combine += "\n" + ", ".join(words
                                    )
    print('Please select a smoothie from our menu', combine)

    print('\n','Enter the number of the smoothie you want to order')

    order = CustomerOrder()
    currentOrder = order.placeOrder()

    print('Is your order correct on the screen?', str(currentOrder))


if __name__ == '__main__':
    main()
