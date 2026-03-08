import requests

API_KEY = "d5W8UWMf1j40MmGX7lNVilNkJBgqUU7LVysZsEr3"


def fetch_data(name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {
        ...
      },
      'locations': [
        ...
      ],
      'characteristics': {
        ...
      }
    },
    """
    url = f'https://api.api-ninjas.com/v1/animals?name={name}'
    response = requests.get(url, headers={'X-Api-Key': API_KEY})
    responce_json = response.json()
    return responce_json
