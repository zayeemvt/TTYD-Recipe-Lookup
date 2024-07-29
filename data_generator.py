from json_reader import readRecipeJSON

def generateIngredientsList(data, printConsole: bool):
    ingredient_list = []

    for item in data:
        for recipe in item["recipe"]:
            for ingredient in recipe:
                if ingredient not in ingredient_list:
                    ingredient_list.append(ingredient)

    if(printConsole):
        print(ingredient_list)
