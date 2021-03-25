from src.Display.ReadSmoothieFile import ReadSmoothieFile

class CustomSmoothie:

    def __init__(self):
        self.selectedIngredients = []

    def createCustomSmoothie(self):

        combine = ""
        continueOrdering = 1

        ingredientsMenu = Menu.smoothieMenu(self, 'Ingredients')

        for words in ingredientsMenu:
            combine += "\n" + ", ".join(words)

        print("Please select the ingredient you would like to add to your custom smoothie\n", combine, "\n")

        while continueOrdering == 1:

            ingredientNumber = int(input("Enter the number of the ingredient you would like"))

            for item in ingredientsMenu:
                if int(item[0]) == ingredientNumber:
                    self.selectedIngredients.append(item[1])
                    print("\nYou have added", item[1], "to your custom smoothie!\nIt currently contains " + ", ".join(self.selectedIngredients))


            continueOrdering = int(input('\nAdd another ingredient? 1 for yes, any other number for no'))


        return("Custom smoothie: " + ", ".join(self.selectedIngredients))
