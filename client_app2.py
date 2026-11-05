import requests

url = "http://localhost:5000/api/items"

response = requests.get(url).json()

print(response)