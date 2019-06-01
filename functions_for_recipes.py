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
        print(data['meals'][INSTRUCTIONS]['strInstructions'])
        i = 1
        n = 21
        while i < n:
            if type(data['meals'][INSTRUCTIONS][f'strIngredient{i}']) == str and \
                    type(data['meals'][INSTRUCTIONS][f'strMeasure{i}']) == str:
                print(data['meals'][INSTRUCTIONS][f'strIngredient{i}'], end='......')
                print(data['meals'][INSTRUCTIONS][f'strMeasure{i}'])
                i += 1
            else:
                i += 1