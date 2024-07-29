from json_reader import readRecipeJSON
from data_generator import generateIngredientsList

if __name__ == "__main__":
    data = readRecipeJSON(False)
    generateIngredientsList(data, True)