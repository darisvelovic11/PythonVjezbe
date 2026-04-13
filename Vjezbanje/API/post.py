import requests

url = "https://jsonplaceholder.typicode.com/users"

novi_korisnik = {
    "name": "Seljo",
    "username": "seljo1968",
    "email": "seljo@gmail.com"
}

response = requests.post(url, json=novi_korisnik)
data = response.json()

print(f"Status kod: {response.status_code}")
print(f"ID novog korisnika: {data['id']}")
print(f"Username novog korisnika: {data['username']}")

