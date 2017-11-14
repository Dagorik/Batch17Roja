import requests

URL_BASE = "https://goodreads-devf-aaron.herokuapp.com/api/v1"

def mi_peticion_post(nombre,apellidos,bio,edad):
	URI = "/authors/"
	URL = URL_BASE + URI
	json_send = {
		"name": nombre,
		"last_name": apellidos,
		"nacionalidad": "MX",
		"biography": bio,
		"gender": "F",
		"age": edad
	}

	response = requests.post(URL,json=json_send)

	return response

respuesta = mi_peticion_post("PYTHON","PYTHON2","ESTE ES UNA PETICION DE PRUEBA",22)
print(respuesta.status_code)
print(respuesta.json())
