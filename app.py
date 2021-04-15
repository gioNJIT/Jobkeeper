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

total_result = data['totalCount']
all_jobs = data['jobs']


def get_job_title(all_jobs):
    return all_jobs['title']

def get_job_location(all_jobs):
    return all_jobs['location']
    
def get_job_salary(all_jobs):
    return all_jobs['salary']
    
def get_job_type(all_jobs):
    return all_jobs['type']

def get_job_link(all_jobs):
    return all_jobs['link']

def get_job_company(all_jobs):
    return all_jobs['company']
    
def get_job_id(all_jobs):
    return all_jobs['id']
    
job_titles = map(get_job_title, all_jobs)
job_locations = map(get_job_location, all_jobs)
job_salaries = map(get_job_salary, all_jobs)
job_types = map(get_job_type, all_jobs)
job_links = map(get_job_link, all_jobs)
job_companies = map(get_job_company, all_jobs)
job_ids = map(get_job_id, all_jobs)

job_details = {
    'total_jobs': total_result,
    'titles' : list(job_titles),
    'locations' : list(job_locations),
    'salaries' : list(job_salaries),
    'types' : list(job_types),
    'links' : list(job_links),
    'companies' : list(job_companies),
    'ids' : list(job_ids),
    
}

print(job_details)

#for job in all_jobs:
#    print(job['title'])

#print(all_jobs)
