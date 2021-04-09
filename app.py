import requests

api_key = 'a7203d29-d277-4d34-a2ba-4b79649682c5'
BASE_URL = 'https://jooble.org/api/a7203d29-d277-4d34-a2ba-4b79649682c5'

params = {
		"keywords": "Accountant",
		"location": "New Jersey",
		"radius": "50",
		"salary": "200000",
		"page": "1"
 }

response = requests.post(BASE_URL, json=params)
data = response.json()

print(data)
