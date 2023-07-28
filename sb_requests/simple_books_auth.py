from random import random

import requests, random

URL = 'https://simple-books-api.glitch.me/api-clients/'


def get_token():
    number = random.randint(1, 999)  # cu instructiunea / metoda asta (se) va genera un nr aleatoriu
    body = {
        "clientName": "Postman",
        "clientEmail": f"valentin{number}@example.com"
    }
    response = requests.post(URL, json=body)
    # print(response)
    # print(response.json())
    return response.json()['accessToken']

# token = get_token()            # pentru a proba token-ul
# get_token()
# print(token)
