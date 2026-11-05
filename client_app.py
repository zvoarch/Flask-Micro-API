import requests

base_url = 'http://localhost:8080'
response1 = requests.get(f'{base_url}/firstten').json()
response2 = requests.get(f'{base_url}/manufacturers').json()
response3 = requests.get(f'{base_url}/cars/prices').json()

print(response1)
print(response2)
print(response3)