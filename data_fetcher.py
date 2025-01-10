import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


def api_data_load(animal_name):
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        return "Error:", response.status_code, response.text


def get_animals_data(animal, skin_type):
    """ Returns a dictionary with the relevant data for each animal """
    full_animals_data = api_data_load(animal)

    animals_data = {}
    for animal in full_animals_data:
        try:
            animal_skin_type = animal["characteristics"]["skin_type"]
        except KeyError:
            animal_skin_type = "not specified"

        if skin_type != animal_skin_type and skin_type != "All":
            continue

        animal_data = {}
        animal_data["taxonomy"] = " - ".join(animal["taxonomy"].values())
        if "characteristics" in animal:
            if "diet" in animal["characteristics"]:
                animal_data["Diet"] = animal["characteristics"]["diet"]
            if "type" in animal["characteristics"]:
                animal_data["Type"] = animal["characteristics"]["type"]
            if "lifespan" in animal["characteristics"]:
                animal_data["Lifespan"] = animal["characteristics"]["lifespan"]
        if "locations" in animal:
            animal_data["Location"] = " and ".join(animal["locations"])
        animals_data[animal["name"]] = animal_data
    return animals_data


