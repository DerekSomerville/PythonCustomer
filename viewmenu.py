def view_menu():
    with open("menu.txt") as file:
        itemsmenu = [line.rstrip() for line in file]
        file.close
    for items in itemsmenu:
        readable = items.split("^")
        print(readable[0] + ",  £" + readable[1])
