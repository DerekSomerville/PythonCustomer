from src.Display.ReadSmoothieFile import ReadSmoothieFile
from src.Display.InputConsole import InputConsole

class CustomSmoothie:

    def __init__(self):
        self.selectedIngredients = []


    def createCustomSmoothie(self):
        userInput = InputConsole()
        combine = ""
        continueOrdering = 1

        ingredientsMenu = ReadSmoothieFile.smoothieFile(self, 'Ingredients')

        for words in ingredientsMenu:
            combine += "\n" + ", ".join(words)

        print("Please select the ingredient you would like to add to your custom smoothie\n", combine, "\n")

        while continueOrdering == 1:

            ingredientNumber = userInput.getInputInt("Enter the number of the ingredient you would like")

            if ingredientNumber >= 1 and ingredientNumber <= len(ingredientsMenu):

                for item in ingredientsMenu:
                    if int(item[0]) == ingredientNumber:
                     self.selectedIngredients.append(item[1])
                     print("\nYou have added", item[1], "to your custom smoothie!\nIt currently contains " + ", ".join(self.selectedIngredients))

            else: print("That's not a valid ingredient! Enter a number from the menu")

            continueOrdering = userInput.getInputInt('\nContinue adding ingredients? Press 1 for yes, any other NUMBER to finish')


        return("Custom smoothie: " + ", ".join(self.selectedIngredients))
