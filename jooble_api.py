'''
This is the jooble API
'''
import os
from dotenv import load_dotenv, find_dotenv
import requests

load_dotenv(find_dotenv())

def get_job_data(param_list): # pylint: disable=R0914
    '''
    This is the job data function
    '''
    job_name = str(param_list[0])
    job_location = str(param_list[1])
    job_radius = str(param_list[2])
    job_salary = str(param_list[3])
    api_key = os.getenv('api_key')
    base_url = 'https://jooble.org/api/' + str(api_key)
    params = {"keywords":job_name, "location":job_location, "radius":job_radius, "salary":job_salary, "page": "1"} # pylint: disable=C0301
    response = requests.post(base_url, json=params)
    data = response.json() # Converting the response into the json
    total_result = data['totalCount']
    all_jobs = data['jobs']
    #All the functions for extracting data from the json response
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
    def get_job_id(all_jobs):
        return all_jobs['id']
    job_titles = map(get_job_title, all_jobs)
    job_locations = map(get_job_location, all_jobs)
    job_salaries = map(get_job_salary, all_jobs)
    job_types = map(get_job_type, all_jobs)
    job_links = map(get_job_link, all_jobs)
    # job_companies = map(get_job_company, all_jobs)
    job_ids = map(get_job_id, all_jobs)
    #returning the all data (List) for all jobs in one dictionary
    return {
        'total_jobs': total_result,
        'titles' : list(job_titles),
        'locations' : list(job_locations),
        'salaries' : list(job_salaries),
        'types' : list(job_types),
        'links' : list(job_links),
        # 'companies' : list(job_companies),
        'ids' : list(job_ids),
    }
