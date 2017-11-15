import requests

URL = "https://goodreads-devf-aaron.herokuapp.com/api/v1/authors/"

def mi_funcion():
	response = requests.get(URL)
	#print(response.json()[0]['biography'])
	lista_jsons = response.json()

	for elemeto_lista in lista_jsons:
		print(type(elemeto_lista))
		print(elemeto_lista['biography'])

		

mi_funcion()