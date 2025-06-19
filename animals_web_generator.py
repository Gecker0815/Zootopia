import json

def read_animals_template():
    """Reads and returns the content of the animal template HTML file."""
    with open("animals_template.html", "r", encoding="utf-8") as fileobj:
        return fileobj.read()


def write_animals_html(new_animal_template):
    """Writes the modified animal template to a new HTML file."""
    with open("animals.html", "w") as fileobj:
        fileobj.write(new_animal_template)


def load_data(file_path):
    """Loads data from a JSON file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def get_animals_string(animals_data, skin_type):
    """Generate an HTML string that lists animal information."""
    output = ""

    output += '<ul class="cards">'
    for animal in animals_data:
        if skin_type is not None and animal["characteristics"].get("type") != skin_type:
          continue
         
        output += '<li class="cards__item">'
        output += f'  <div class="card__title">{animal["name"]}</div>'
        output += '  <div class="card__text">'
        output += '    <ul>'
        output += f'      <li><strong>Diet:</strong> {animal["characteristics"]["diet"]}</li>'
        output += f'      <li><strong>Location:</strong> {animal["locations"][0]}</li>'
        if "type" in animal["characteristics"]:
            output += f'      <li><strong>Type:</strong> {animal["characteristics"]["type"]}</li>'
        output += '    </ul>'
        output += '  </div>'
        output += '</li>'
    output += '</ul>'

    return output


def choose_animal_skin_type(animals_data):
    """Prompts the user to select an animal skin type from a dynamically generated list."""
    skin_types_list = []

    for animal in animals_data:
        skin_type = animal["characteristics"]["skin_type"]
        if skin_type not in skin_types_list:
            skin_types_list.append(skin_type)
      
    print("****Animal skin type list****")
    print("0. without skin type")
    for index, skin_type in enumerate(skin_types_list):
        print(f"{index + 1}. {skin_type}")

    while True:
        skin_type_number = input("Enter skin type number: ")

        if skin_type_number.isdigit():
            selected_index = int(skin_type_number)
            if selected_index == 0:
                return None
            elif 1 <= selected_index <= len(skin_types_list):
                return skin_types_list[selected_index - 1]
            else:
                print("Number out of range! Please enter a valid number.")
        else:
            print("Please enter a number!")


def main():
    """Main function to process animal data and generate an HTML file."""
    animals_data = load_data('animals_data.json')
    skin_type = choose_animal_skin_type(animals_data)
    output = get_animals_string(animals_data, skin_type)
    animal_template = read_animals_template()
    animal_template = animal_template.replace("__REPLACE_ANIMALS_INFO__", output)
    write_animals_html(animal_template)


if __name__ == "__main__":
    main()