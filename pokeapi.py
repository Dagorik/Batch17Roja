import requests

BASE_URL = "http://pokeapi.co/api/v2/"
URI_POKEMON_1 = "pokemon/1"

URL= BASE_URL + URI_POKEMON_1

response = requests.get(URL)

diccionario = response.json()
lista = diccionario['forms']
diccioanrio2 = lista[0]
print(diccioanrio2['name'])

