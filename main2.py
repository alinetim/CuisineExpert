from functions_for_recipes import get_a_recipe, get_all_possible_countries, get_recipes_by_area, food_text_analysis

while True:
    answer = input('Do you want to cook by yourself or go to restaurant?(Choose: recipe/ restaurant):')
    if answer == 'recipe':
        get_all_possible_countries()
        country = input('Enter preferable country:')
        get_recipes_by_area(country)
        recipe = input('Choose recipe:')
        ingredients = get_a_recipe(recipe)
        total_calories = 0
        total_fat = 0
        total_carbs = 0
        total_sugar = 0
        tota_protein = 0
        i = 0
        while i < (len(ingredients) - 1):
            data = food_text_analysis(ingredients[i] + ' ' + ingredients[i + 1])
            try:
                total_calories += data['calories']
            except KeyError:
                pass
            try:
                total_fat += data['totalNutrients']['FAT']['quantity']
            except KeyError:
                pass
            try:
                 total_carbs += data['totalNutrients']['CHOCDF']['quantity']
            except KeyError:
                pass
            try:
                  total_sugar += data['totalNutrients']['SUGAR']['quantity']
            except KeyError:
                pass
            try:
                tota_protein += data['totalNutrients']['PROCNT']['quantity']
            except KeyError:
                pass
            i += 2
        print(total_calories)