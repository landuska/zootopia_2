import json
import re
import requests

API_KEY = "d5W8UWMf1j40MmGX7lNVilNkJBgqUU7LVysZsEr3"


def load_one_animal(name):
    """ Load animal_info about one animal """

    url = f'https://api.api-ninjas.com/v1/animals?name={name}'
    response = requests.get(url, headers={'X-Api-Key': API_KEY})
    responce_json = response.json()
    return responce_json


def load_all_animals():
    """ Load all animals"""

    url = 'https://api.api-ninjas.com/v1/animals'
    response = requests.get(url, headers={'X-Api-Key': API_KEY})
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


def user_input(html_page: str):
    """ Choice of animal and write a new HTML page with it
    or write a new HTML page with all animals
    """

    while True:
        user_choice = input(
            f"Please enter an animal you want to see: ").strip().lower()

        if not user_choice:
            print("Please enter animal, not an empty string: ")
            continue

        animals = load_one_animal(user_choice)
        html_with_animals = html_page.replace("__REPLACE_ANIMALS_INFO__", animals_info(animals))
        save_html("../zootopia_2/animals_2.html", html_with_animals)
        return


def main():
    html_page = load_html("../zootopia_2/animals_template_2.html")
    user_input(html_page)


if __name__ == "__main__":
    main()
