from src.Display.ReadSmoothieFile import ReadSmoothieFile
from src.Display.InputConsole import InputConsole


class CustomSmoothie:

    def __init__(self):
        self.userInput = InputConsole()
        self.selectedIngredients = []
        self.continueOrderingFlag = True
        self.continueRemovingFlag = True
        self.ingredientsMenu = ReadSmoothieFile.smoothieFile(self, 'Ingredients')

    def printMenu(self, menu):

        combine = ""
        for words in menu:
            combine += "\n" + ", ".join(words)
        print(combine)

    def createCustomSmoothie(self):

        self.printMenu(self.ingredientsMenu)

        while self.continueOrderingFlag:

            userActionChoice = self.userInput.getInputInt('\nBegin/continue adding ingredients?\nEnter 1 for YES, '
                                                          '\nEnter 2 to REMOVE AN INGREDIENT,'
                                                          '\nEnter ANY OTHER NUMBER to finalise your smoothie '
                                                          'and add it to your order.\n')
            if userActionChoice == 2:
                self.continueRemovingFlag = True
                self.removeIngredient()
                if self.continueOrderingFlag == False:
                    return "Custom smoothie: " + ", ".join(self.selectedIngredients)
            elif userActionChoice != 1:
                return "Custom smoothie: " + ", ".join(self.selectedIngredients)

            ingredientNumber = self.userInput.getInputInt("Enter the number of the ingredient you would like to add")
            if 1 <= ingredientNumber <= len(self.ingredientsMenu):
                for item in self.ingredientsMenu:
                    if int(item[0]) == ingredientNumber:
                        self.selectedIngredients.append(item[1])
                        print("\nYou have added", item[1], " to your custom smoothie!\nIt currently contains",
                              ", ".join(self.selectedIngredients))
            else:
                print("That's not a valid ingredient! Enter a number from the menu")

        return "Custom smoothie: " + ", ".join(self.selectedIngredients)

    def removeIngredient(self):

        while self.continueRemovingFlag:

            for ingredient in self.selectedIngredients:
                print(str(self.selectedIngredients.index(ingredient)) + " " + ingredient)
            removedIngredient = self.userInput.getInputInt("Enter the number of the ingredient you would like to remove\n")

            try:
                print("You have removed:", self.selectedIngredients.pop(removedIngredient))
                print("Your smoothie now contains: " + ", ".join(self.selectedIngredients))

            except IndexError:
                print("Invalid ingredient\n")

            userActionChoice = self.userInput.getInputInt("\nEnter 1 to remove another ingredient,\n"
                                                          "Enter 2 to add more ingredients\n"
                                                          "Enter any other NUMBER to finalise your smoothie "
                                                          "and add it to your order.\n")
            if userActionChoice == 1:
                continue
            elif userActionChoice == 2:
                self.printMenu(self.ingredientsMenu)
                self.continueRemovingFlag = False
                self.continueOrderingFlag = True
            else:
                self.continueRemovingFlag = False
                self.continueOrderingFlag = False

        return

