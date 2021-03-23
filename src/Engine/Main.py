from src.Display.ReadSmoothieFile import Menu
from src.Entities.CustomerOrder import CustomerOrder


def main():
    menu = Menu()
    customerMenu = menu.Smoothie_Menu()

    print('Please select a smooth from our menu', '\n', str(customerMenu)
          .replace('[', '').replace(']', '').replace(',', '\n').replace("'", ''))

    print('Enter the number of the smoothie you want to order')

    order = CustomerOrder()
    currentOrder = order.placeOrder()

    print('Is your order correct on the screen?', str(currentOrder))


if __name__ == '__main__':
    main()
