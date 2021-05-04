'''
This is the app.py
'''
import json
import os
import requests
from dotenv import load_dotenv, find_dotenv
from flask import Flask, send_from_directory, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from Jooble_api import get_job_data




app = Flask(__name__, static_folder='./build/static')


load_dotenv(find_dotenv())

API_KEY = os.getenv('api_key')
BASE_URL = 'https://jooble.org/api/' + str(API_KEY)



# Point SQLAlchemy to your Heroku database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
# Gets rid of a warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# IMPORTANT: This must be AFTER creating db variable to prevent
# circular import issues
import models  # pylint: disable=wrong-import-position



cors = CORS(app, resources={r"/*": {"origins": "*"}})


app = Flask(__name__, static_folder='./build/static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


cors = CORS(app, resources={r"/*": {"origins": "*"}})

records = []


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
    user_id = str(temp_id['clientId'])
    user_email = temp_id['email']
    
    records.append(user_id)
    records.append(user_email)
  
    
    return "Test"
@app.route('/api/v1/job/searchJob', methods=['GET'])
def search_job():
    '''
    This is a job search function
    '''
    parameterList = []
    
    if 'occupation' in request.args:
        parameterList.append(request.args['occupation'])
        parameterList.append(request.args['location'])
        parameterList.append(request.args['radius'])
        parameterList.append(request.args['salary'])
        
        job_details = get_job_data(parameterList)
        #print(job_details)
        alljob_dict = {}
        if job_details['total_jobs'] <= 5:
            total = job_details['total_jobs']
        else:
            total = 5
        for job in range(0, total):
            alljob_dict.update({job: [job_details['titles'][job], job_details['locations'][job], job_details['salaries'][job], job_details['ids'][job]]})  # pylint: disable=C0301
        #title_arr = job_details['titles'][0]
        print(alljob_dict)
        return jsonify(alljob_dict)
    return "Something went wrong"
    
@app.route('/api/v1/job/getfavJob', methods=['GET'])
def getfav_job():
    '''
    This is the favorite function
    '''
    favjob_dict = []
    #print(request.args)
    if 'id' in request.args:
        player = db.session.query(  # pylint: disable=E1101 
        models.Person).filter_by(id= str(request.args['id']) ).first()
        print(player.favorites)
        #print(player.favorites)
        
        for x in range(len(player.favorites)):
            
            jobquery= models.Jobs.query.filter_by(job_id=player.favorites[x]).first()
            favjob_dict.append([jobquery.job_id,jobquery.job_title,jobquery.job_location,jobquery.job_salary])
            #print(favjob_dict[x])
        
        print(favjob_dict)
        return jsonify(favjob_dict)
        
        
    else:
        print("Could not find it")
        return "Something went wrong"

@app.route('/api/v1/job/getAppliedJob', methods=['GET'])
def getAppliedJob():
    appliedjobDict={}
    if 'id' in request.args:
        player = models.Person.query.filter_by(id=request.args["id"]).first()
        
        print("received id:")
        print(id)
        print("applied list from id:")
        print(player.applied)
        
        for x in range(len(player.applied)):
            
            jobquery= models.Jobs.query.filter_by(job_id=player.applied[x]).first()
            appliedjobDict[x]=[jobquery.job_id,jobquery.job_title,jobquery.job_location,jobquery.job_salary]
            print(appliedjobDict[x])
        
        
        return jsonify(appliedjobDict)
        
        
    else:
        print("Could not find it")
        return "Something went wrong"

    


@app.route('/api/v1/job/Favorites', methods=['POST'])
def add_favourites():
    """this function is called in jobs.js and adds a FAVORITED job to jobs tables"""
    temp_list = []
    data = request.get_json()
    #data = request.args['favorite'].split(',')
    fav_job_title = data['title']
    fav_job_location = data['location']
    fav_job_salary = data['salary']


    fav_job_id = str(data['id'])

    #all_fav = models.Person.query.filter_by(id=user_id).first()
    all_fav = db.session.query(  # pylint: disable=E1101 
        models.Person).filter_by(id= records[0] ).first()
    
    if all_fav is None:
        print("Record is not founded")
        new_entry = models.Person(id=records[0], email=records[1], favorites=[fav_job_id], applied=[])    
        db.session.add(new_entry)
        db.session.commit()
    else:
        if fav_job_id not in all_fav.favorites:
            temp_list = all_fav.favorites
            client_id = all_fav.id
            temp_email = all_fav.email
            temp_applied = all_fav.applied
            db.session.delete(all_fav)
            db.session.commit()
            
            temp_list.append(str(fav_job_id))
            
            
            #if all_fav.favorites is None:
            new_entry = models.Person(id=client_id, email=temp_email,favorites=temp_list,applied=temp_applied)    
            db.session.add(new_entry)
            db.session.commit()
        else:
            print("ID is already favorited")
        
        
    favorited = db.session.query(  # pylint: disable=E1101 
        models.Jobs).filter_by(job_id= fav_job_id ).first()
    
    if favorited is None:
        print("Job is not founded")
        new_entry = models.Jobs(job_id=fav_job_id, job_title=fav_job_title, job_location=fav_job_location, job_salary=fav_job_salary)    
        db.session.add(new_entry)
        db.session.commit()
    else:
        print("Job is already in the database")
    
    
    return "Something went wrong"







@app.route('/api/v1/job/Applied', methods=['POST'])
def add_Applied():
    """this function is called in jobs.js and adds an APPLIED job to jobs tables"""
    temp_list = []
    data = request.get_json()
    #data = request.args['favorite'].split(',')
    appl_job_title = data['title']
    appl_job_location = data['location']
    appl_job_salary = data['salary']
    appl_job_id = data['id']


    
    #all_fav = models.Person.query.filter_by(id=user_id).first()
    all_applied = db.session.query(  # pylint: disable=E1101 
        models.Person).filter_by(id= records[0] ).first()
    
    if all_applied is None:
        print("Record is not founded") 
        new_entry = models.Person(id=records[0], email=records[1],favorites=[] , applied=[appl_job_id])    
        db.session.add(new_entry)
        db.session.commit()
    else:
        if appl_job_id not in all_applied.applied:
            temp_list = all_applied.applied
            client_id = all_applied.id
            temp_email = all_applied.email
            temp_fav = all_applied.favorites
            db.session.delete(all_applied)
            db.session.commit()
            
            temp_list.append(str(appl_job_id))
            
            
            #if all_fav.favorites is None:
            new_entry = models.Person(id=client_id, email=temp_email,favorites=temp_fav,applied=temp_list)    
            db.session.add(new_entry)
            db.session.commit()
        else:
            print("ID is already in applied list")

        
    applied = db.session.query(  # pylint: disable=E1101 
        models.Jobs).filter_by(job_id= appl_job_id ).first()
    
    if applied is None:
        print("Job is not founded")
        new_entry = models.Jobs(job_id=appl_job_id, job_title=appl_job_title, job_location=appl_job_location, job_salary=appl_job_salary)    
        db.session.add(new_entry)
        db.session.commit()
    else:
        print("Job is already in the database")
    
    
    return "Something went wrong"




if __name__ == "__main__":
    app.run(
        host=os.getenv('IP', '0.0.0.0'),
        port=8081,
        debug=True,
        use_reloader=True
        )
