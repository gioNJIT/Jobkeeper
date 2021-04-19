import functools
import json
import os
from dotenv import load_dotenv,find_dotenv
import flask
import requests
from authlib.client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery
import google_auth
from Jooble_api import get_job_data
from flask_socketio import SocketIO
from flask_cors import CORS

load_dotenv(find_dotenv())

parameterList = []


app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = os.getenv("FN_FLASK_SECRET_KEY", default=False)
app.register_blueprint(google_auth.app)

cors = CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app,
                    cors_allowed_origins="*",
                    json=json,
                    manage_session=False)



@app.route('/')
def index():
    if not google_auth.is_logged_in():
        Login=google_auth.login()
        return  Login
        
    #if google_auth.is_logged_in():
    else:
        #user_info = google_auth.get_user_info()
        #return '<div>You are currently logged in as ' + user_info['given_name'] + '<div><pre>' + json.dumps(user_info, indent=4) + "</pre>"
        return "You Loged in"
    
    
    
@socketio.on('UserLoggedIn')
def on_UserLoggedIn():
    socketio.emit('UserLoggedIn', broadcast=True, include_self=True)
    print("user has logged in")
    
    
    
@socketio.on('connect')
def on_connected():
    """
    handle when user connects to server
    """
    print('User connected!')   
    
    
    
@socketio.on('sendParams')
def receiveParams(data):
    parameterList = data["userParams"]
    job_details = get_job_data(parameterList)
    print(job_details)
    
    
    
    
socketio.run(
    app,
    host=os.getenv('IP', '0.0.0.0'),
    port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
)

