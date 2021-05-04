import functools
import json
import os
from dotenv import load_dotenv,find_dotenv
from flask import Flask, send_from_directory, request, jsonify, Response
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
import models  # pylint: disable=wrong-import-position
user_id = 123321







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

@app.route('/api/v1/job/userInfo', methods=['POST'])
def userInfo():
    print("hello")
    temp_id = request.get_json()
    user_id = temp_id['clientId']
    print(user_id)
    return "Test"
    
    
@app.route('/api/v1/job/searchJob', methods=['GET'])
def searchJob():
    parameterList = []
    if 'occupation' in request.args:
        parameterList.append(request.args['occupation'])
        parameterList.append(request.args['location'])
        parameterList.append(request.args['radius'])
        parameterList.append(request.args['salary'])
        
        job_details = get_job_data(parameterList)
        #print(job_details)
        alljob_dict = {}
        if(job_details['total_jobs'] <= 5):
            total = job_details['total_jobs']
        else:
            total = 5
            
        
        for job in range(0, total):
            alljob_dict.update({job: [job_details['titles'][job], job_details['locations'][job], job_details['salaries'][job], str(job_details['ids'][job])]})
        #alljob_dict = {0:[job_details['titles'][0], job_details['locations'][0], job_details['salaries'][0], job_details['ids'][0]]}
        title_arr = job_details['titles'][0]
        #print(alljob_dict)
        return jsonify(alljob_dict)
        
        
    else:
        print("Could not find it")
        return "Something went wrong"
        
    #print("Params received")


@app.route('/api/v1/job/getfavJob', methods=['GET'])
def getfavJob():
    favjobDict={}
    if 'id' in request.args:
        player = models.Person.query.filter_by(id=request.args["id"]).first()
        
        print("received id:")
        print(id)
        print("favorites list from id:")
        print(player.favorites)
        
        for x in range(len(player.favorites)):
            
            jobquery= models.Jobs.query.filter_by(job_id=player.favorites[x]).first()
            favjobDict[x]=[jobquery.job_id,jobquery.job_title,jobquery.job_location,jobquery.job_salary]
            print(favjobDict[x])
        
        
        return jsonify(favjobDict)
        
        
    else:
        print("Could not find it")
        return "Something went wrong"



    
@app.route('/api/v1/job/Favorites', methods=['GET'])
def add_favourites():
    temp_list = []
    data = request.args['favorite'].split(',')
    #print(data[4])
    fav_job_id = data[4]
    #print(all_entry)
    
    
    #all_fav = models.Person.query.filter_by(id=user_id).first()
    all_fav = db.session.query(  # pylint: disable=E1101 
        models.Person).filter_by(id=user_id ).first()
    #print(all_fav.favorites)
    temp_list = all_fav.favorites
    client_id = all_fav.id
    temp_email = all_fav.email
    temp_applied = all_fav.applied
    db.session.delete(all_fav)
    db.session.commit()
    
    temp_list.append(str(fav_job_id))
    print(temp_list)
    print(client_id)
    print(temp_email)
    print(temp_applied)
    
    #if all_fav.favorites is None:
    new_entry = models.Person(id=client_id, email=temp_email,favorites=temp_list,applied=temp_applied)    
    db.session.add(new_entry)
    db.session.commit()
        
    #print(all_fav.favorites)
    
    
    return "Something went wrong"


"""
"EXAMPLE FUNCTION TO BE USED TO RETREIVE DATA FROM DATABASE"    
def add_users():
    player = models.Person.query.filter_by(id=123321).first()
    if player is None:
        print("could not find id number")
        #addplayer = models.Person(username=data['user'], score=100)
        #DB.session.add(addplayer)  # pylint: disable=no-member
        #DB.session.commit()  # pylint: disable=no-member
    else:
        print("player")
        print(player.id)
    
    
# @socketio.on('UserLoggedIn')
# def on_UserLoggedIn():
#     socketio.emit('UserLoggedIn', broadcast=True, include_self=True)
#     print("user has logged in")
    
    
#add_users()"""

    
    
    
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