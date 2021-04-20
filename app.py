import functools
import json
import os
from dotenv import load_dotenv,find_dotenv
import flask
import requests
from Jooble_api import get_job_data
from flask_socketio import SocketIO
from flask_cors import CORS

load_dotenv(find_dotenv())

parameterList = []


app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


cors = CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app,
                    cors_allowed_origins="*",
                    json=json,
                    manage_session=False)




    
    
    
    
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

