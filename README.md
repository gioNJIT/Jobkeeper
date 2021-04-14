# JOB FIND APP

## Requirements
1. `npm install`
2. `pip install -r requirements.txt`

## Launching Google API
First, `pip install -r requirements.txt`
In order to get the Google API working, you need to Create a project and enable the API on Google Cloud Platform (GCP), `https://developers.google.com/workspace/guides/create-project`,
and then creat credentials for your project, `https://developers.google.com/workspace/guides/create-credentials#web`.
Upon following the steps you should have your client id and client secret. Then you can create a .env file and do the following steps,
`export FN_AUTH_REDIRECT_URI=http://localhost:8080/google/auth`
`export FN_BASE_URI=http://localhost:8080`
`export FN_CLIENT_ID=THE CLIENT ID WHICH YOU CREATED EARLIER`
`export FN_CLIENT_SECRET=THE CLIENT SECRET WHICH YOU CREATED EARLIER`
`export FLASK_APP=app.py`
`export FLASK_DEBUG=1`
`export FN_FLASK_SECRET_KEY=SOMETHING RANDOM AND SECRET`
In your terminal type, `python -m flask run -p 8080`, to get it run.
