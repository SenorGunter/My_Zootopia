
import json


def load_data(file_path):
    """ Loads JSON"""
    with open(file_path, "r") as fileobj:
        return json.load(fileobj)


def load_html_template(file_path):
    """ Loads HTML file """
    with open(file_path, "r") as fileobj:
        return fileobj.read()


def get_animals_data(skin_type):
    """ Returns a dictionary with the relevant data for each animal """
    full_animals_data = load_data("animals_data.json")

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


def serialize_animal(animal_name, animal_data):
    """ Returns the HTML code for the information """
    html_output = '<li class="cards__item">\n'
    html_output += f'<div class="card__title">{animal_name}</div>\n'
    html_output += f'<p class="card__taxonomy">{animal_data["taxonomy"]}</p>\n'
    html_output += '<ul class="card__info">\n'
    for key, value in animal_data.items():
        if key != "taxonomy":
            html_output += f'<li><strong>{key}:</strong> {value}</li>\n'
    html_output += '</ul>\n</li>\n'
    return html_output


def get_possible_skin_types():
    """ Returns the possible skin types """
    full_animals_data = load_data("animals_data.json")
    skin_types = set()
    for animal in full_animals_data:
        if "characteristics" in animal and "skin_type" in animal["characteristics"]:
            skin_types.add(animal["characteristics"]["skin_type"])
    return list(skin_types)


def get_user_input():
    """ Asks the user for the skin type """
    skin_types = get_possible_skin_types()
    print("Possible skin types:")
    print("All")
    for skin_type in skin_types:
        print(skin_type)
    while True:
        try:
            skin_type = input("Enter the skin type of the animals: ")
            if skin_type in skin_types or skin_type == "All":
                return skin_type
            else:
                print("Invalid skin type. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    new_html = load_html_template("animals_template.html")
    skin_type = get_user_input()
    animals_data = get_animals_data(skin_type)

    html_animals_data = ""
    for animal_name, animal_data in animals_data.items():
        html_animals_data += serialize_animal(animal_name, animal_data)

    new_html = new_html.replace("__REPLACE_ANIMALS_INFO__", html_animals_data)
    with open("animals.html", "w") as fileobj:
        fileobj.write(new_html)