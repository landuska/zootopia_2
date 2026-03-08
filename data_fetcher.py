import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


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
