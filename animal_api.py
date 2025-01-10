import requests

def api_data_load(animal_name):
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)
    response = requests.get(api_url, headers={'X-Api-Key': 'syAiwBvjXARymJ8ivwSZ6A==9nwhsKDrekK2cUoO'})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        return "Error:", response.status_code, response.text


