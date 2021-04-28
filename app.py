import functools
import json
import os
from dotenv import load_dotenv,find_dotenv
from flask import Flask, send_from_directory
import requests
from Jooble_api import get_job_data
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_folder='./build/static')


load_dotenv(find_dotenv())

api_key = os.getenv('api_key')
BASE_URL = 'https://jooble.org/api/' + str(api_key)



# Point SQLAlchemy to your Heroku database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
# Gets rid of a warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# IMPORTANT: This must be AFTER creating db variable to prevent
# circular import issues
from models import Person







parameterList = []


app = Flask(__name__, static_folder='./build/static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', defaults={"filename": "index.html"})
@app.route('/<path:filename>')
def index(filename):
    '''
    This is a index function
    '''
    return send_from_directory('./build', filename)

    
    
    
@app.route('/api/v1/job/searchJob', methods=['GET'])
def searchJob():
    print("Params received")
    return "test"
    
    
# @socketio.on('UserLoggedIn')
# def on_UserLoggedIn():
#     socketio.emit('UserLoggedIn', broadcast=True, include_self=True)
#     print("user has logged in")
    
    
    

    
    
    
# @socketio.on('sendParams')
# def receiveParams(data):
#     parameterList = data["userParams"]
#     job_details = get_job_data(parameterList)
#     title_arr = job_details['titles']
#     socketio.emit( "Updated_details",title_arr, broadcast=True, include_self=True)
#     print(job_details['titles'])
    
    
if __name__ == "__main__":    
    app.run(
        host=os.getenv('IP', '0.0.0.0'),
        port=8081,
        debug=True,
        use_reloader=True
        )