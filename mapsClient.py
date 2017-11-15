import googlemaps
from datetime import datetime

now = datetime.now()
print(now)

gmaps = googlemaps.Client(key = 'AIzaSyASVMg4pk12-uuvjKTTfkaN7BqUs-9j0xE')

origen = "Impact Hub, Av. Álvaro Obregón 168, Cuauhtémoc, Roma Norte, 06700 Ciudad de México, CDMX"
destino = "Zócalo, Centro Histórico, Centro, 06000 Ciudad de México, CDMX"

direccion = gmaps.directions(origen,
							destino,
							mode = 'driving',
							departure_time=now)
print(direccion)