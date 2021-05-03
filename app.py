'''
This is the app.py
'''
import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, send_from_directory, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from Jooble_api import get_job_data




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


APP = Flask(__name__, static_folder='./build/static')
APP.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


CORS = CORS(APP, resources={r"/*": {"origins": "*"}})


@APP.route('/', defaults={"filename": "index.html"})
@APP.route('/<path:filename>')
def index(filename):
    '''
    This is a index function
    '''
    return send_from_directory('./build', filename)

@APP.route('/api/v1/job/userInfo', methods=['POST'])
def user_info():
    '''
    This is the user information function
    '''
    print(request.get_json())
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
        print(job_details)
        alljob_dict = {}
        if job_details['total_jobs'] <= 5:
            total = job_details['total_jobs']
        else:
            total = 5
        for job in range(0, total):
            alljob_dict.update({job:[job_details['titles'][job], job_details['locations'][job], job_details['salaries'][job], job_details['ids'][job]]})
        #title_arr = job_details['titles'][0]
        print(alljob_dict)
        return jsonify(alljob_dict)
    return "Something went wrong"
@APP.route('/api/v1/job/getfav_job', methods=['GET'])
def getfav_job():
    '''
    This is the favorite function
    '''
    favjob_dict = {}
    if 'id' in request.args:
        player = models.Person.query.filter_by(id=request.args["id"]).first()
        print("received id:")
        print(id)
        print("favorites list from id:")
        print(player.favorites)
        for fav in range(len(player.favorites)):
            jobquery = models.Jobs.query.filter_by(job_id=player.favorites[fav]).first()
            favjob_dict[fav] = [jobquery.job_id, jobquery.job_title, jobquery.job_location, jobquery.job_salary]
            print(favjob_dict[fav])
        return jsonify(favjob_dict)
    return "Something went wrong"
@APP.route('/api/v1/job/Favorites', methods=['GET'])
def add_favourites():
    '''
    This is the add to favorites function
    '''
    data = request.args['favorite'].split(',')
    print(data[0])
    return "Something went wrong"
if __name__ == "__main__":
    APP.run(
        host=os.getenv('IP', '0.0.0.0'),
        port=8081,
        debug=True,
        use_reloader=True
        )
