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


def printing_all_names(data):
    for foxes in data:
        print(f'Name: {foxes.get("name", "unknown")}')
        print(f'Diet: {foxes["characteristics"].get("diet", "unknown")}')
        print(f'Location: {foxes["locations"][0]}')
        print(f'Type: {foxes["characteristics"].get("type", "unknown")}')


def main():
    animals_data = load_data('animals_data.json')
    printing_all_names(animals_data)

if __name__ == "__main__":
    main()