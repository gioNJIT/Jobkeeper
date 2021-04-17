import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

api_key = os.getenv('api_key')
BASE_URL = 'https://jooble.org/api/' + api_key

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
