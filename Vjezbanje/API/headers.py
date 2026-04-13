import requests
url = "https://httpbin.org/post"
podaci = {"ime": "Daris"}

response = requests.post(url, json=podaci)
data = response.json()

print(data["headers"])