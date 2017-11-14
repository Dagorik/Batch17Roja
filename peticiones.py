import requests

response = requests.get('http://api.open-notify.org/iss-now.json')
print(response.status_code)
print(response.ok)
print(response.headers['content-type'])
print(response.text)

print("--------------------------")
diccionario = response.json()
print(diccionario['timestamp'])