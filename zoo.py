import requests

API_KEY = "d5W8UWMf1j40MmGX7lNVilNkJBgqUU7LVysZsEr3"
NAME = "tttttttt"


def get_animals():
    api_url = f'https://api.api-ninjas.com/v1/animals?name={NAME}'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        # animal_info = response.json()[0]
        print(response)
    else:
        print("Error:", response.status_code, response.text)


get_animals()
