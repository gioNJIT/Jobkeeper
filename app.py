'''
This is the app.py
'''
import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, send_from_directory, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from jooble_api import get_job_data




APP = Flask(__name__, static_folder='./build/static')


load_dotenv(find_dotenv())

API_KEY = os.getenv('api_key')
BASE_URL = 'https://jooble.org/api/' + str(API_KEY)



# Point SQLAlchemy to your Heroku database
APP.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
# Gets rid of a warning
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DB = SQLAlchemy(APP)

# IMPORTANT: This must be AFTER creating db variable to prevent
# circular import issues
import models  # pylint: disable=wrong-import-position



CORS = CORS(APP, resources={r"/*": {"origins": "*"}})


APP = Flask(__name__, static_folder='./build/static')
APP.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

RECORDS = []


@APP.route('/', defaults={"filename": "index.html"})
@APP.route('/<path:filename>')
def index(filename):
    '''
    This is a index function
    '''
    return send_from_directory('./build', filename)
@APP.route('/api/v1/job/user_info', methods=['POST'])
def user_info():
    '''
    This is a user information function
    '''
    temp_id = request.get_json()
    user_id = str(temp_id['clientId'])
    user_email = temp_id['email']
    RECORDS.append(user_id)
    RECORDS.append(user_email)
    return "Test"
@APP.route('/api/v1/job/searchJob', methods=['GET'])
def search_job():
    '''
    This is a job search function
    '''
    parameter_list = []
    if 'occupation' in request.args:
        parameter_list.append(request.args['occupation'])
        parameter_list.append(request.args['location'])
        parameter_list.append(request.args['radius'])
        parameter_list.append(request.args['salary'])
        job_details = get_job_data(parameter_list)
        alljob_dict = {}
        if job_details['total_jobs'] <= 5:
            total = job_details['total_jobs']
        else:
            total = 5
        for job in range(0, total):
            alljob_dict.update({job: [job_details['titles'][job], job_details['locations'][job], job_details['salaries'][job], job_details['ids'][job], job_details['links'][job]]})  # pylint: disable=C0301
        print(alljob_dict)
        return jsonify(alljob_dict)
    return "Something went wrong"
@APP.route('/api/v1/job/getfavJob', methods=['GET'])
def getfav_job():
    '''
    This is the favorite function
    '''
    favjob_dict = []
    if 'id' in request.args:
        player = DB.session.query(models.Person).filter_by(id=str(request.args['id'])).first() # pylint: disable=E1101
        if player.favorites is None:
            return "Nothing is Favorited"
        for fav in range(len(player.favorites)):
            jobquery = models.Jobs.query.filter_by(job_id=player.favorites[fav]).first()
            favjob_dict.append([jobquery.job_id, jobquery.job_title, jobquery.job_location, jobquery.job_salary, jobquery.job_link]) # pylint: disable=C0301
        return jsonify(favjob_dict)
    return "Something went wrong"
@APP.route('/api/v1/job/get_applied_job', methods=['GET'])
def get_applied_job():
    '''
    This is the get the applied job function
    '''
    appliedjob_dict = []
    if 'id' in request.args:
        player = models.Person.query.filter_by(id=str(request.args["id"])).first()
        if player.applied is None:
            print("List is empty")
            return "Applied list is empty"
        for fav in range(len(player.applied)):
            jobquery = models.Jobs.query.filter_by(job_id=player.applied[fav]).first()
            appliedjob_dict.append([jobquery.job_id, jobquery.job_title, jobquery.job_location, jobquery.job_salary, jobquery.job_link]) # pylint: disable=C0301
        print(appliedjob_dict)
        return jsonify(appliedjob_dict)
    return "Something went wrong"
@APP.route('/api/v1/job/Favorites', methods=['POST'])
def add_favourites():
    """this function is called in jobs.js and adds a FAVORITED job to jobs tables"""
    temp_list = []
    data = request.get_json()
    fav_job_title = data['title']
    fav_job_location = data['location']
    fav_job_salary = data['salary']
    fav_job_id = str(data['id'])
    fav_job_link = data['link']
    all_fav = DB.session.query(models.Person).filter_by(id=RECORDS[0]).first() # pylint: disable=E1101
    if all_fav is None:
        print("Record is not founded")
        new_entry = models.Person(id=RECORDS[0], email=RECORDS[1], favorites=[fav_job_id], applied=[]) # pylint: disable=C0301,C0303 
        DB.session.add(new_entry) # pylint: disable=E1101
        DB.session.commit() # pylint: disable=E1101
    else:
        if fav_job_id not in all_fav.favorites:
            temp_list = all_fav.favorites
            client_id = all_fav.id
            temp_email = all_fav.email
            temp_applied = all_fav.applied
            DB.session.delete(all_fav) # pylint: disable=E1101
            DB.session.commit() # pylint: disable=E1101
            temp_list.append(str(fav_job_id))
            new_entry = models.Person(id=client_id, email=temp_email, favorites=temp_list, applied=temp_applied)   # pylint: disable=C0301,C0303 
            DB.session.add(new_entry) # pylint: disable=E1101
            DB.session.commit() # pylint: disable=E1101
        else:
            print("ID is already favorited")
    favorited = DB.session.query(models.Jobs).filter_by(job_id=fav_job_id).first() # pylint: disable=E1101
    if favorited is None:
        print("Job is not founded")
        new_entry = models.Jobs(job_id=str(fav_job_id), job_title=fav_job_title, job_location=fav_job_location, job_salary=fav_job_salary, job_link=fav_job_link)  # pylint: disable=C0301,C0303
        DB.session.add(new_entry) # pylint: disable=E1101
        DB.session.commit() # pylint: disable=E1101
    else:
        print("Job is already in the database")
    return "Something went wrong"
@APP.route('/api/v1/job/Applied', methods=['POST'])
def add_applied():
    """this function is called in jobs.js and adds an APPLIED job to jobs tables"""
    temp_list = []
    data = request.get_json()
    appl_job_title = data['title']
    appl_job_location = data['location']
    appl_job_salary = data['salary']
    appl_job_id = str(data['id'])
    appl_job_link = str(data['link'])
    all_applied = DB.session.query(models.Person).filter_by(id=RECORDS[0]).first() # pylint: disable=E1101
    if all_applied is None:
        print("Record is not founded")
        new_entry = models.Person(id=RECORDS[0], email=RECORDS[1], favorites=[], applied=[appl_job_id]) # pylint: disable=C0301
        DB.session.add(new_entry) # pylint: disable=E1101
        DB.session.commit() # pylint: disable=E1101
    else:
        if appl_job_id not in all_applied.applied:
            temp_list = all_applied.applied
            client_id = all_applied.id
            temp_email = all_applied.email
            temp_fav = all_applied.favorites
            DB.session.delete(all_applied) # pylint: disable=E1101
            DB.session.commit() # pylint: disable=E1101
            temp_list.append(str(appl_job_id))
            new_entry = models.Person(id=client_id, email=temp_email, favorites=temp_fav, applied=temp_list) # pylint: disable=C0301
            DB.session.add(new_entry) # pylint: disable=E1101
            DB.session.commit() # pylint: disable=E1101
        else:
            print("ID is already in applied list")
    applied = DB.session.query(models.Jobs).filter_by(job_id=appl_job_id).first() # pylint: disable=E1101
    if applied is None:
        print("Job is not founded")
        new_entry = models.Jobs(job_id=appl_job_id, job_title=appl_job_title, job_location=appl_job_location, job_salary=appl_job_salary, job_link=appl_job_link)  # pylint: disable=C0301
        DB.session.add(new_entry) # pylint: disable=E1101
        DB.session.commit() # pylint: disable=E1101
    else:
        print("Job is already in the database")
    return "Something went wrong"
if __name__ == "__main__":
    APP.run(
        host=os.getenv('IP', '0.0.0.0'),
        port=8081,
        debug=True,
        use_reloader=True
        )
