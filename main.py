from functions import get_id, find_cuisine, restaurant_search
import urllib.parse, requests


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
