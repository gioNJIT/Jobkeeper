from dotenv import load_dotenv,find_dotenv
import os
import json
import requests

load_dotenv(find_dotenv())

def get_job_data(paramList):
    jobName = str(paramList[0])
    jobLocation = str(paramList[1])
    jobRadius = str(paramList[2])
    jobSalary = str(paramList[3])

    api_key = os.getenv('api_key')
    BASE_URL = 'https://jooble.org/api/' + str(api_key)
    
    
    # Setting all the query parameter for the API call
    params = {
    		"keywords": jobName,
    		"location": jobLocation,
    		"radius": jobRadius,
    		"salary": jobSalary,
    		"page": "1"
     }

     
    
    response = requests.post(BASE_URL, json=params)  #Making a call to the Joooble API using POST request
    data = response.json() # Converting the response into the json
    #print(data)
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
    
    # def get_job_company(all_jobs):
    #     return all_jobs['company']
        
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
