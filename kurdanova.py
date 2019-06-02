import requests


def food_text_analysis():

    app_id = 'b25a621b'
    app_key = '164b53282bbeda25555bac62065493ad'

    response = requests.get(f"https://api.edamam.com/api/nutrition-data?app_id={app_id}&app_key={app_key}&ingr=1%20large%20apple")
    if response.status_code == 200:
        data = response.json()
        return data['totalNutrients']