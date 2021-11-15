from datetime import datetime
import recipe

class book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = recipes_list
        # put default variables : https://stackoverflow.com/questions/4841782/python-constructor-and-default-value

    def get_recipe_by_name(self, name):
        #"Prints a recipe with the name \texttt{name} and returns the instance"
        pass
    def get_recipes_by_types(self, recipe_type):
        #"Get all recipe names for a given recipe_type " 
        pass
    def add_recipe(self):\
        creaName = input("CREATION - Please enter the recipe's name you want to create:" + f"\n")
        creaDifficulty = input("Please enter the difficulty of this recipe from 1 to 5:" + f"\n")
        creatTime = input("Please enter the time needed (in minutes) to realise your recipe:" + f"\n")
        creaIngredients = input("Please enter the ingredients needed to do this recipe:" + f"\n")
        creadescription = input("Please enter the description of this recipe:" + f"\n")
        creaRecipe_type = input("Please enter the type of meal of your recipe:" + f"\n")
        creaName = recipe(creaName, creaDifficulty, creatTime, creaIngredients, creadescription, creaRecipe_type)
        print("The cookbook contains a new recipe : " + creaName.name + " !!" +f"\n")

Italian = book()
book.add_recipe()