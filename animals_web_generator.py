import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


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