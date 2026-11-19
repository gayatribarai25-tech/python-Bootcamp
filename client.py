import requests

BASE_URL = "http://127.0.0.1:8001"

response = requests.get(f"{BASE_URL}/events")
print(response.json())

response = requests.get(f"{BASE_URL}/events/Monday")
print(response.json())

response = requests.get(f"{BASE_URL}/events/Wednesday")
print(response.json())

response = requests.get(f"{BASE_URL}/events/Friday")
print(response.json())

response = requests.get(f"{BASE_URL}/events/monday")
print(response.json())

response = requests.get(f"{BASE_URL}/events/MONDAY")
print(response.json())

response = requests.get(f"{BASE_URL}/events/Tuesday")
print(response.json())