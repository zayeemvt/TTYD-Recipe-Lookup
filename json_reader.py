import json

def readRecipeJSON(printConsole: bool):
    f = open('Recipes.json')
    data = json.load(f)

    if printConsole:
        for item in data:
            print(f'#{item["id"]}: {item["name"]}')
            for recipe in item["recipe"]:
                print(recipe)

    f.close()

    return data
