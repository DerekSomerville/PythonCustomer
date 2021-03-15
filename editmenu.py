def addmenu(nameitem, pricepound = 0, pricepence = 0):
    try:
        pricepound = int(pricepound)
    except ValueError:
        print("a number is required here")
        return
    try:
        pricepence = int(pricepence)
    except ValueError:
        print("a number is required here")
        return
    if len(str(pricepence)) == 1:
        pricepence = "0" + str(pricepence)
    newitem =  nameitem + "^" + str(pricepound) + "." + str(pricepence)
    file = open("menu.txt", "a")
    file.write("\n"+ newitem)
    file.close

def addhelp():
    print('To add an item to the menu type addmenu("name of item", pounds, pence) \n'
          'an example of this would be additem(donut,1,50) to ad a donut at £1.50')
