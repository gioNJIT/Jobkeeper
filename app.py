import functools
import json
import os
from dotenv import load_dotenv,find_dotenv
from flask import Flask, send_from_directory
import requests
from Jooble_api import get_job_data
from flask_socketio import SocketIO
from flask_cors import CORS

load_dotenv(find_dotenv())

parameterList = []


app = Flask(__name__, static_folder='./build/static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


cors = CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app,
                    cors_allowed_origins="*",
                    json=json,
                    manage_session=False)


@app.route('/', defaults={"filename": "index.html"})
@app.route('/<path:filename>')
def index(filename):
    '''
    This is a index function
    '''
    return send_from_directory('./build', filename)

    
    
    
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
    
    
    
    
if __name__ == "__main__":  
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
    )

