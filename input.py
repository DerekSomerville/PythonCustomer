




def orderInput():
    menu = {}
    with open("menu.txt", "r") as file:
        for data in file.readlines():
            data = data.lower()
            data = data.strip()
            data = data.split("^")
            menu[data[0]] = data[1]




    counter = 0
    print(menu)
    total = []
    while counter == 0:
        userOrder = input("Please select an item off the menu you would like to purchase")
        if userOrder in menu:
            amount = int(input("Please enter the amount of" + " " + userOrder + " " + "you would like to buy"))
            print("Okay! I have added to your total")

            quantityCost = float(menu[userOrder])


            total.append(userOrder)
            total.append(amount)
            total.append(quantityCost*amount)

            print(total)
            continue
        else:
            print("Sorry we dont sell that here")



orderInput()