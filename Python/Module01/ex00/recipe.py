class recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

        creaName = input("CREATION - Please enter the recipe's name you want to create:" + f"\n")
        creaName = input("Please enter the difficulty of this recipe from 1 to 5:" + f"\n")
        creatTime = input("Please enter the time needed (in minutes) to realise your recipe:" + f"\n")
        creaIngredients = input("Please enter the ingredients needed to do this recipe:" + f"\n")
        creadescription = input("Please enter the description of this recipe:" + f"\n")
        creaRecipe_type = input("Please enter the type of meal of your recipe:" + f"\n")
    
        if not isinstance(self.name, str):
            print("Name must be a string")
            exit()
        
        if not isinstance(self.cooking_lvl, int) or not isinstance(self.cooking_time, int):
            print("cooking_lvl and cooking_time must be integers")
            exit()
        try: 
            if cooking_time < 0:
                print("the cooking time must be positive")
                exit()
        except: 
            exit()

        if not 1 <= cooking_lvl <= 5:
            print("the cooking level must be between 1 to 5.")

        if not isinstance(self.ingredients, list):
            print("ingredients must be a list")
            exit()
        
        for i in self.ingredients:
            if not isinstance(i, str):
                print("all ingredients in the list of ingredients must be a string")
                exit()

        if not isinstance(self.description, str):
            print("description must be a string")
            exit()

        if not isinstance(self.recipe_type, str):
            print("recipe_type must be a str")
            exit()
        
        if not (recipe_type == "starter" or recipe_type == "lunch" or recipe_type == "dessert"):
            print("recipe_type can only take these values : 'starter', 'lunch', 'dessert'")
            exit()            

    def __str__ (self):
        return "The recipe you are consulting is : {}. \n\
From one to five, the level of difficult of this recipe is {}, and you will need {} minutes to do it.\
You need all this ingredients: {}. This recipe is better for {}. {}.".format(self.name, self.cooking_lvl, self.cooking_time, ', '.join(self.ingredients), self.recipe_type, self.description)

#    def printName(self): #self in the function refer to the class recipe above. It could have called differently.
#        print("Name of the recipe: " + self.name)


cake = recipe("cakem", 3, 30, ["flour", "sugar", "chocolate"], "This is a delicious cake", "lunch")
print("The cookbook contains a new recipe : " + cake.name + " !!" +f"\n")

#cake.printName()
print(cake)

