import requests
#https://api.github.com/users/Dagorik
#http://api.open-notify.org/iss-now.json
response = requests.get("https://api.github.com/users/Dagorik")
print(response.status_code)
print(response.headers)
print(response.text)
diccionario = response.json()
print(diccionario['name'])

