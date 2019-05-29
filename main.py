from functions import get_id, find_cuisine, restaurant_search

city = input('Enter a city: ')
while True:

    city_id = get_id(city)
    cuisine = input('Enter a cuisine: ')
    if not cuisine:
        break
    else:
        cuisine_id_num = find_cuisine(cuisine, city_id)
        result = restaurant_search(city_id, cuisine_id_num, f'restaurants_{cuisine}.txt')
