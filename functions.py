import requests


headers = {
        "Accept": "application/json",
        "user-key": "43a81700d6c6dbcd2f03aeabddd8bad7"
    }


def get_id(city):

    p = {
        "q": f"{city}"
    }

    response = requests.get(f'https://developers.zomato.com/api/v2.1/cities', headers=headers, params=p)
    data = response.json()

    for i in range(len(data['location_suggestions'])):
        if data['location_suggestions'][i]['country_id'] == 216:
            return data['location_suggestions'][i]['id']


def find_cuisine(cuisine, city_id):

    p = {
        "city_id": f"{city_id}"
    }

    response = requests.get(f'https://developers.zomato.com/api/v2.1/cuisines', headers=headers, params=p)
    data = response.json()

    for i in range(len(data['cuisines'])):
        if data['cuisines'][i]['cuisine']['cuisine_name'] == cuisine:
            return data['cuisines'][i]['cuisine']['cuisine_id']


def restaurant_search(city_id, cuisine_id, path):

    p = {
        "entity_id": f"{city_id}",
        "entity_type": "city",
        "count": 10,
        "cuisines": f"{cuisine_id}"
    }

    response = \
        requests.get\
            (f'https://developers.zomato.com/api/v2.1/search', headers=headers, params=p)
    data = response.json()

    with open(path, 'w') as f:

        for i in range(len(data['restaurants'])):
            f.write(f"Name: {data['restaurants'][i]['restaurant']['name']}\n")
            f.write(f"Address: {data['restaurants'][i]['restaurant']['location']['address']}\n")
            f.write(f"Average cost for two: {data['restaurants'][i]['restaurant']['currency']}"
                    f"{data['restaurants'][i]['restaurant']['average_cost_for_two']}\n")
            f.write(f"Rating: {data['restaurants'][i]['restaurant']['user_rating']['aggregate_rating']}\n")
            f.write("-----------------------------------------------------------------------\n")
