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
        with open(path, 'w') as f:
            for i in range(len(result['restaurants'])):
                f.write(f"Name: {result['restaurants'][i]['restaurant']['name']}\n"
                f"Address: {result['restaurants'][i]['restaurant']['location']['address']}\n"
                f"Average cost for two: {result['restaurants'][i]['restaurant']['currency']}\n"
                f"{result['restaurants'][i]['restaurant']['average_cost_for_two']}\n"
                f"Rating: {result['restaurants'][i]['restaurant']['user_rating']['aggregate_rating']}\n"
                f"-----------------------------------------------------------------------\n")
