import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyASVMg4pk12-uuvjKTTfkaN7BqUs-9j0xE')

now = datetime.now()

directions_result = gmaps.directions("Impact Hub, Av. Álvaro Obregón 168, Cuauhtémoc, Roma Norte, 06700 Ciudad de México, CDMX",
                                     "Zócalo, Centro Histórico, Centro, 06000 Ciudad de México, CDMX",
                                     mode="driving",
                                     departure_time=now)

print(directions_result)
