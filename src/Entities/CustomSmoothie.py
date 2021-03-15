class CustomSmoothie():

    #Initialises a CustomSmoothie instance. We pass a list of ingredients created by the user in.
    #We limit the maximum number of ingredients using the if statement. This wouldnt be necessary if this was enforced in the smoothie creation module
    #How do we restrict this paramater to only take a list?
    def __init__(self, ingredients):
        if len(ingredients) < 6:
            self.ingredients = ingredients

    #Returns a string describing the CustomSmoothie. This string can be appended to the customer's Order/Receipt
    def describeCustomSmoothie(self):
        ingredientsList = ", ".join(self.ingredients)
        return f"Custom Smoothie: {ingredientsList}"

#Example of creating a CustomSmoothie instance, ingredient are passed in as a list.
mySmoothie = CustomSmoothie(['Banana', 'Bacon', 'Apple', 'Tea', 'Coffee'])

print(mySmoothie.describeCustomSmoothie())
