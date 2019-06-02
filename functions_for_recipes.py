import requests
INSTRUCTIONS = 0


def get_recipes_by_area(country):
    response = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?a={country}")
    if response.status_code == 200:
        data = response.json()
        for i in range(len(data["meals"])):
            print(data["meals"][i]["strMeal"])


def get_all_possible_countries():
    response = requests.get('https://www.themealdb.com/api/json/v1/1/list.php?a=list')
    if response.status_code == 200:
        data = response.json()
        for i in range(len(data["meals"])):
            print(data['meals'][i]['strArea'])


def get_a_recipe(name_of_recipe):
    response = requests.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={name_of_recipe}')
    if response.status_code == 200:
        data = response.json()
        i = 1
        n = 21
        ingredients = []
        while i < n:
            if (data['meals'][INSTRUCTIONS][f'strIngredient{i}'] == "") or \
                    (data['meals'][INSTRUCTIONS][f'strIngredient{i}'] is None) and \
                    (data['meals'][INSTRUCTIONS][f'strMeasure{i}'] == "") or \
                    (data['meals'][INSTRUCTIONS][f'strMeasure{i}'] is None):
                i += 1
            else:
                print(data['meals'][INSTRUCTIONS][f'strIngredient{i}'], end='......')
                print(data['meals'][INSTRUCTIONS][f'strMeasure{i}'])
                ingredients.append(data['meals'][INSTRUCTIONS][f'strIngredient{i}'])
                i += 1
        print(data['meals'][INSTRUCTIONS]['strInstructions'])
        return ingredients
