from functions_for_recipes import get_a_recipe, get_all_possible_countries, get_recipes_by_area, food_text_analysis
from functions_for_restaurants import get_id, find_cuisine, restaurant_search

while True:
    answer = input('Do you want to cook by yourself or go to restaurant?(Choose: recipe/ restaurant/ "enter" to finish):')
    if not answer:
        break
    elif answer == 'recipe':
        get_all_possible_countries()
        while True:
            country = input('Enter preferable cuisine:')
            try:
                recipes = get_recipes_by_area(country)
                break
            except:
                print('Сuisine not found. Please try again!')
                continue
        while True:
            recipe = input('Choose recipe:')
            if recipe in recipes:
                break
            else:
                print("The recipe is not found. Please try again!")
        ingredients, instructions = get_a_recipe(recipe)
        total_calories = 0
        total_fat = 0
        total_carbs = 0
        total_sugar = 0
        tota_protein = 0
        i = 0
        print('Procesing .', end = '', flush = True)
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
            if i < (len(ingredients) - 1):
                print(' .', end = '', flush = True)
            else:
                print(' .', flush = True)
        with open(f'{recipe}.txt', 'w', encoding = 'UTF-8') as f:
            f.write(f'Recipe:\n')
            for line in instructions:
                if len(line) > 4:
                    f.write(f'{line}\n')
            f.write(f"Bon appetit!!\n"
            f"-----------------------------------------------------------------------\n"
            f'Recipe analysis:\n'
            f'Total calories: {total_calories} kcal.\n'
            f'Total fat: {total_fat:.2f} g.\n'
            f'Total carbs: {total_carbs:.2f} g.\n'
            f'Total protein: {tota_protein:.2f} g.\n'
            f'Total sugar: {total_sugar:.2f} g.')
    elif answer == 'restaurant':
        city = input('Enter a city in USA: ')
        if not city:
            continue
        try:
            city_id = get_id(city)
        except KeyError:
            pass

        cuisine = input('Which cuisine you would like to try?(f.e. Russian): ')
        cuisine = cuisine.capitalize()
        if not cuisine:
            continue
        try:
            cuisine_id_num = find_cuisine(cuisine, city_id)
        except KeyError:
            pass
        try:
            restaurants = restaurant_search(city_id, cuisine_id_num)
        except KeyError:
            pass
        with open(f'{cuisine}_restaurants.txt', 'w', encoding='UTF-8') as f:
            for i in range(len(restaurants['restaurants'])):
                f.write(f"Name: {restaurants['restaurants'][i]['restaurant']['name']}\n"
                f"Address: {restaurants['restaurants'][i]['restaurant']['location']['address']}\n"
                f"Average cost for two: {restaurants['restaurants'][i]['restaurant']['currency']}"
                f"{restaurants['restaurants'][i]['restaurant']['average_cost_for_two']}\n"
                f"Rating: {restaurants['restaurants'][i]['restaurant']['user_rating']['aggregate_rating']}\n"
                f"-----------------------------------------------------------------------\n")
    else:
        print('Wrong answer. Please try again!')
        continue
