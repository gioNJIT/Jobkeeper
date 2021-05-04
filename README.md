# JOB FIND APP

# Heroku Link:
[App Link](https://guarded-bayou-27051.herokuapp.com/)

## Requirements
1. `npm install`
2. `npm install react-google-login`
3. `npm install react-router-dom`
4. `pip install -r requirements.txt`

## Launching Google API
First, `pip install -r requirements.txt`
In order to get the Google API working, you need to Create a project and enable the API on Google Cloud Platform (GCP),
[create a project](https://developers.google.com/workspace/guides/create-project),
and then create credentials for your project, 
[create credentials ](https://developers.google.com/workspace/guides/create-credentials#web).
Upon following the steps you should have your client id and client secret. 
> Create a .env file and do the following steps,
>>`export FN_AUTH_REDIRECT_URI=http://localhost:8080/google/auth`
>>`export FN_BASE_URI=http://localhost:8080`
>>`export FN_CLIENT_ID=THE CLIENT ID WHICH YOU CREATED EARLIER`
>>`export FN_CLIENT_SECRET=THE CLIENT SECRET WHICH YOU CREATED EARLIER`
>>`export FLASK_APP=app.py`
>>`export FLASK_DEBUG=1`
>>`export FN_FLASK_SECRET_KEY=SOMETHING RANDOM AND SECRET`


# JOB FIND APP
1. `Use your API key from jooble api_key={your api key}`
2. `Use your Database URL DATABASE_URL={your api key}`


## Run Application
1. Run command in terminal (in your project directory): `python app.py`
2. Run command in another terminal, `cd` into the project directory, and run `npm run start`
3. Preview web page in browser '/'

In your terminal type, `python -m flask run -p 8080`, to get it run (if `npm sun start` does not work).
