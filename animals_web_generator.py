import json

def read_animals_template():
    """Reads and returns the content of the animal template HTML file."""
    with open("animals_template.html", "r") as fileobj:
        return fileobj.read()

def write_animals_html(new_animal_template):
    """Writes the modified animal template to a new HTML file."""
    with open("animals.html", "w") as fileobj:
        fileobj.write(new_animal_template)

def load_data(file_path):
    """Loads data from a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

def get_animals_string(animals_data):
    """Formats animal data into a readable string."""
    output = ""

    for animal in animals_data:
        output += f"Name: {animal['name']}\n"
        output += f"Diet: {animal['characteristics']['diet']}\n"
        output += f"Location: {animal['locations'][0]}\n"
        if 'type' in animal['characteristics']:
            output += f"Type: {animal['characteristics']['type']}\n\n"

    return output

def main():
    """Main function to process animal data and generate an HTML file."""
    animals_data = load_data('animals_data.json')
    output = get_animals_string(animals_data)
    animal_template = read_animals_template()
    animal_template = animal_template.replace("__REPLACE_ANIMALS_INFO__", output)
    write_animals_html(animal_template)

if __name__ == "__main__":
    main()