import requests

URL = "https://maps.googleapis.com/maps/api/directions/json?origin=Impact+Hub+Roma+Norte+MX&destination=Zócalo+Plaza+de+la+Constitucion+MX&key=AIzaSyASVMg4pk12-uuvjKTTfkaN7BqUs-9j0xE"
mapa = requests.get(URL)
print(mapa.status_code)
print(mapa.json())