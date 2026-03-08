import json
import re
import requests

API_KEY = "d5W8UWMf1j40MmGX7lNVilNkJBgqUU7LVysZsEr3"
NAME = "Fox"


def load_data():
    """ Load a JSON file """

    api_url = f'https://api.api-ninjas.com/v1/animals?name={NAME}'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    responce_json = response.json()
    return responce_json


def load_html(file_path):
    """ Load a HTML file """

    with open(file_path, "r") as file:
        return file.read()


def save_html(file_path, content):
    """ Save a HTML file """

    with open(file_path, "w") as file:
        file.write(content)


def add_if_exists(title: str, characteristic: str):
    """ Add to HTML a characteristic if it exists """

    if characteristic:
        return f"<li><strong>{title}: </strong>{characteristic}</li>\n"
    return ""


def serialize_animal(all_info_of_one_animal: tuple):
    """ Serialize an animal """

    output_string = ''
    location, name, diet, temperament, color, lifespan, animal_type, skin_type = all_info_of_one_animal

    output_string += '<li class="cards__item">'
    output_string += f'<div class="card__title">{name}</div><br>\n'
    output_string += f'<div class="card__text">\n'
    output_string += "<ul>\n"
    output_string += add_if_exists("Diet", diet)
    output_string += add_if_exists("Location", location)
    output_string += add_if_exists("Temperament", temperament)
    output_string += add_if_exists("Color", color)
    output_string += add_if_exists("Lifespan", lifespan)
    output_string += add_if_exists("Group", animal_type)
    output_string += add_if_exists("Skin_type", skin_type)
    output_string += "</ul>\n"
    output_string += '</div>\n'
    output_string += "</li>"

    return output_string


def animals_info(animals: list):
    """ Get all info about animals for uploading to the site"""

    output = ''
    for animal in animals:
        location = ", ".join(animal.get("locations", []))
        name = re.sub(r'[^a-zA-Z0-9 ]', '', animal.get("name", "").strip())
        characteristics = animal.get("characteristics", {})
        diet = characteristics.get("diet", "").strip()
        temperament = characteristics.get("temperament", "").strip()
        color = characteristics.get("color", "").strip()
        lifespan = characteristics.get("lifespan", "").strip().replace("â€“", " - ")
        animal_type = characteristics.get("group", "").strip()
        skin_type = characteristics.get("skin_type", "").strip()

        all_info_of_one_animal = location, name, diet, temperament, color, lifespan, animal_type, skin_type

        output += serialize_animal(all_info_of_one_animal)

    return output


def get_skin_types(animals: list):
    """ Get all skin types"""

    skin_types = set()
    for animal in animals:
        characteristics = animal.get("characteristics", {})
        skin_type = characteristics.get("skin_type", "").strip().lower()
        if skin_type:
            skin_types.add(skin_type)

    return skin_types


def get_animals_with_skin_type(animals: list, user_choice: str):
    """ Get all animals with the same skin type """

    animals_with_skin_type = []
    for animal in animals:
        characteristics = animal.get("characteristics", {})
        skin_type = characteristics.get("skin_type", "").strip().lower()
        if skin_type == user_choice:
            animals_with_skin_type.append(animal)
    return animals_with_skin_type


def user_input(skin_types: set, html_page: str, animals: list):
    """ Choice of skin type and write a new HTML page with animals with this skin type
        or write a new HTML page with all animals
    """

    while True:
        user_choice = input(
            f"Please enter animals skin_type from {skin_types} or 'all' if you want sea all animals: ").strip().lower()

        if not user_choice:
            print("Please enter animals skin_type, not an empty string: ")
            continue

        if user_choice in skin_types:
            animals_with_skin_type = get_animals_with_skin_type(animals, user_choice)
            html_with_animals = html_page.replace("__REPLACE_ANIMALS_INFO__", animals_info(animals_with_skin_type))
            save_html("../zootopia_2/animals_2.html", html_with_animals)
            return
        elif user_choice == "all":
            html_with_animals = html_page.replace("__REPLACE_ANIMALS_INFO__", animals_info(animals))
            save_html("../zootopia_2/animals_2.html", html_with_animals)
            return
        else:
            print(f"Your skin_type is not in {skin_types}")
            continue


def main():
    animals_data = load_data()
    set_of_skin_types = get_skin_types(animals_data)
    html_page = load_html("../zootopia_2/animals_template_2.html")
    user_input(set_of_skin_types, html_page, animals_data)


if __name__ == "__main__":
    main()
