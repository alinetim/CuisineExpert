import urllib.parse, requests
INSTRUCTIONS = 0


def get_recipes_by_area(country):
    response = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?a={country}")
    if response.status_code == 200:
        data = response.json()
        recipes = []
        for i in range(len(data["meals"])):
            recipes.append(data["meals"][i]["strMeal"])
        return recipes


def get_all_possible_countries():
    countries = []
    response = requests.get('https://www.themealdb.com/api/json/v1/1/list.php?a=list')
    if response.status_code == 200:
        data = response.json()
        for i in range(len(data["meals"])):
            countries.append(data['meals'][i]['strArea'])
        return countries


def get_a_recipe(name_of_recipe):
    response = requests.get(f'https://www.themealdb.com/api/json/v1/1/search.php?s={name_of_recipe}')
    if response.status_code == 200:
        data = response.json()
        i = 1
        n = 21
        ingredients = []
        main_info = []
        while i < n:
            if (data['meals'][INSTRUCTIONS][f'strIngredient{i}'] == "") or \
                    (data['meals'][INSTRUCTIONS][f'strIngredient{i}'] is None) and \
                    (data['meals'][INSTRUCTIONS][f'strMeasure{i}'] == "") or \
                    (data['meals'][INSTRUCTIONS][f'strMeasure{i}'] is None):
                i += 1
            else:
                main_info.append((data['meals'][INSTRUCTIONS][f'strIngredient{i}'] + '......' + data['meals'][INSTRUCTIONS][f'strMeasure{i}']))
                ingredients.append(data['meals'][INSTRUCTIONS][f'strMeasure{i}'])
                ingredients.append(data['meals'][INSTRUCTIONS][f'strIngredient{i}'] + ',')
                i += 1
        instruction = data['meals'][INSTRUCTIONS]['strInstructions']
        instruction = instruction.split('.')
        for sentence in instruction:
            main_info.append(sentence.replace('\n', '').replace('\r', '').strip(' ') + '.')
        return ingredients, main_info


def food_text_analysis(recipe):

    app_id = '23c3cc5b'
    app_key = '40422d573ba553cda8ae7536b1d6f300'
    urllib.parse.quote(recipe)

    response = requests.get(f"https://api.edamam.com/api/nutrition-data?app_id={app_id}&app_key={app_key}&ingr={recipe}")
    if response.status_code == 200:
        data = response.json()
        return data
