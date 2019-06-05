import requests
headers = {
        "Accept": "application/json",
        "user-key": "mykey"
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


def restaurant_search(city_id, cuisine_id):

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
    return data
