from functions_for_recipes import get_a_recipe, get_all_possible_countries, get_recipes_by_area, food_text_analysis
from functions_for_restaurants import get_id, find_cuisine, restaurant_search

while True:
    answer = input('Do you want to cook by yourself or go to restaurant?(Choose: recipe/ restaurant):')
    if not answer:
        break
    elif answer == 'recipe':
        get_all_possible_countries()
        country = input('Enter preferable country:')
        recipes = get_recipes_by_area(country)
        recipe = input('Choose recipe:')
        if recipe not in recipes:
            print(f"{recipe} can't be found. Please try again!")
            break
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
    elif answer == 'restaurant':
        city = input('Enter a city: ')
        while True:

            city_id = get_id(city)
            cuisine = input('Enter a cuisine: ')
            if not cuisine:
                break
            else:
                cuisine_id_num = find_cuisine(cuisine, city_id)
                restaurants = restaurant_search(city_id, cuisine_id_num, f'restaurants_{cuisine}.txt')

                with open(path, 'w') as f:
                    for i in range(len(restaurants['restaurants'])):
                        f.write(f"Name: {restaurants['restaurants'][i]['restaurant']['name']}\n"
                        f"Address: {restaurants['restaurants'][i]['restaurant']['location']['address']}\n"
                        f"Average cost for two: {restaurants['restaurants'][i]['restaurant']['currency']}\n"
                        f"{restaurants['restaurants'][i]['restaurant']['average_cost_for_two']}\n"
                        f"Rating: {restaurants['restaurants'][i]['restaurant']['user_rating']['aggregate_rating']}\n"
                        f"-----------------------------------------------------------------------\n")
    else:
        print('Wrong answer')
        continue