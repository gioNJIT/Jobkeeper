import functools
import json
import os
from dotenv import load_dotenv,find_dotenv
import flask

from authlib.client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery

import google_auth
load_dotenv(find_dotenv())
app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = os.getenv("FN_FLASK_SECRET_KEY", default=False)

app.register_blueprint(google_auth.app)

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
    
    #return google_auth.logout()
    
    
app.run(
    host=os.getenv('IP',"0.0.0.0"),
    port=int(os.getenv("PORT",8080)),
    debug=True,
    )
