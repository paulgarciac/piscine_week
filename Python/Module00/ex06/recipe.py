
cookbook = {"sandwich": {'ingredients': 'Bread, butter, ham', 'meal': 'lunch', 'prep_time': '10min'},
    "cake" : {'ingredients': 'Farine, Eggs, Chocolate', 'meal': 'dessert', 'prep_time': '60min'},
    "salad" : {'ingredients': 'Tomato, Letuce, Cucumber', 'meal': 'lumch', 'prep_time': '15min'}}

def isInDict(searchedKey, dict):
    for key in dict.keys():
        if searchedKey == key:
            return(True)
    print("Not in the cookbook, going back to the menu")



def selectNumber():

    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    numSelected = input()
    try:
        if 1 <= float(numSelected) <= 5:
            print("in 1 to 5")
        else:
            print("Only the numbers from 1 to 5")
            selectNumber()
    except:
        print("Only numbers in da menu")
        selectNumber()


    if numSelected == "1": #Create a recipe
        creaName = input("CREATION - Please enter the recipe's name you want to create:" + f"\n")
        creaIngredients = input("CREATION - Please enter the ingredients needed to do this recipe:" + f"\n")
        creatMeal = input("CREATION - Please enter the type of meal of your recipe:" + f"\n")
        creatTime = input("CREATION - Please enter the time needed (in minutes) to realise your recipe:" + f"\n")
        cookbook[creaName] = {'ingredients': creaIngredients, 'meal': creatMeal, 'prep_time': creatTime + "min"}
        print("the cookbook contains a new recipe : " + creaName + " !!")
        selectNumber()

    if numSelected == "2": #Delete a recipe
        delet = input("DELETION - Please enter the recipe's name you want to delete:" + f"\n")
        if isInDict(delet, cookbook):
            del cookbook[delet]
            print("the recipe " + delet + " was deleted :-( ")
        selectNumber()

    if numSelected == "3": #Print a recipe
        recipe = input("GET DETAILS - Please enter the recipe's name to get its details:" + f"\n")
        if isInDict(recipe, cookbook):
            print("Recipe for " + recipe + ":")
            print("Ingredients list:", cookbook[recipe]["ingredients"])
            print("To be eaten for ", cookbook[recipe]["meal"], ".", sep="")
            print("Takes", cookbook[recipe]["prep_time"], "of cooking.")
        selectNumber()

    if numSelected == "4": #Print the cookbook
        print("This cookbook contains recipes to do :")
        for key in cookbook.keys():
            print(key)
        selectNumber()

    if numSelected == "5": #Quit
        print("Cookbook closed.")
        exit()

selectNumber()