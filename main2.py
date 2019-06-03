from functions_for_recipes import get_a_recipe, get_all_possible_countries, get_recipes_by_area, food_text_analysis

while True:
    answer = input('Do you want to cook by yourself or go to restaurant?(Choose: recipe/ restaurant):')
    if answer == 'recipe':
        get_all_possible_countries()
        country = input('Enter preferable country:')
        get_recipes_by_area(country)
        recipe = input('Choose recipe:')
        ingredients = get_a_recipe(recipe)
        string_ingr = ' '.join(ingredients)
        print(string_ingr)
        food_text_analysis('500g Beef Fillet,')

