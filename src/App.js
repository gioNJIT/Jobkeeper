import React, { Fragment } from "react";
import './style.css';
import Login from './Login';
import Logout from './Logout';

import { ListItem } from './ListItem';
import  { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Link, Switch, useParams, Redirect } from "react-router-dom";
import { Jobs } from './Jobs';
import { Fav } from './FavoritePage';
import { Appliedfunct } from './AppliedPage';
import { GoogleLogin } from 'react-google-login';
//import fetch from 'isomorphic-fetch';
const BASE_URL = "/api/v1/job"
var clientId = 
process.env.REACT_APP_GOOGLE_API_KEY;



function App() {
  

 function sendUserDataToServer(userID, firstName, user_email) {
    const url = BASE_URL + "/userInfo";
    var data = JSON.stringify({
      "clientId":userID,
      "firstName":firstName,
      "email" : user_email
      
    });
  fetch(url, {
  method: 'POST', // or 'PUT'
  headers: {
    'Content-Type': 'application/json'
  },
  body: data,
})
.then(response => {
  console.log(response);
  return response.json();
})
.then(data => {
  console.log('Success:', data);
})
.catch((error) => {
  console.error('Error:', error);
});
}

 const [idFavApplied, setidFavApplied] = useState("");

function Login() {
  const onSuccess = (res) => {
    console.log('Login Success: currentUser:', res.profileObj);
    setIsAuthenticated(true);
    clientId = res.profileObj["googleId"];
    var googleId = res.profileObj["googleId"];
    var firstName = res.profileObj["givenName"];
    var user_email = res.profileObj["email"];
    
    setidFavApplied(googleId);
    sendUserDataToServer(googleId, firstName, user_email);
  };

  const onFailure = (res) => {
    console.log('Login failed: res:', res);
    setIsAuthenticated(false);
    
  };
  
  

  return (
    <div>
      <GoogleLogin
        clientId={clientId}
        buttonText="Login"
        onSuccess={onSuccess}
        onFailure={onFailure}
        setIsAuthenticated={onSuccess}
        //cookiePolicy={'single_host_origin'}
        style={{ marginTop: '100px' }}
        isSignedIn={true}
      />
    </div>
  );
}

   
    const jobDataTest = "this is a job posting"; //this is mocking the job posting data that will be passed to the components
    const [isAuthenticated, setIsAuthenticated] = useState(false); //thi is mocking the login authentication. change to false to test
    
    
  function handleBackgroundHome() {
    document.body.style.backgroundImage = "url('https://ak.picdn.net/shutterstock/videos/15071320/thumb/4.jpg') ";
    // document.body.style.backgroundRepeat = "repeat-y";
    // document.body.style.backgroundPosition = "0px 150px";
  };
  
  function handleBackgroundFavorites() {
    document.body.style.backgroundImage = "url('https://i.pinimg.com/736x/96/da/38/96da382665b28aff01e7ffd0d88454b5.jpg')";
  };
  
  function handleBackgroundApplied() {
    document.body.style.backgroundImage = "url('https://www.clipartmax.com/png/small/1-11037_green-check-mark-transparent.png')";
  }
  
  
  function handleBackgroundLogin() {
    document.body.style.backgroundImage = "url('')";
  }
  
    function handleBackgroundLogout() {
    document.body.style.backgroundImage = "url('')";
  }
  
  
  console.log(isAuthenticated);
  
  return (
    <Router>  
        <div>
        <nav>
            <Link onClick={handleBackgroundHome} class="button" to="/Home">Home</Link>|
            <Link onClick={handleBackgroundApplied} class="button" to="/AppliedPage.js">Applied</Link>|
            <Link onClick={handleBackgroundLogin} class="button" to="/Login">Login</Link>|
            <Link onClick={handleBackgroundFavorites} class="button" to="/FavoritePage.js">Favorite</Link>|
            <Link onClick={handleBackgroundLogout} class="button" to="/Logout">Logout</Link>
        </nav>
        <Switch>
            <Route path="/Login"  component={Login} />
            
      
            {
            isAuthenticated ? 
            <div>
            
            <Route path="/Home" component={Home} />
            <Route path="/AppliedPage.js">  <Appliedfunct id = { idFavApplied } /> </Route>
            <Route path="/FavoritePage.js">  <Fav id = { idFavApplied } />   </Route>
            <Route path="/Logout"  component={Logout} />
            </div>
             : <Redirect to="/Login" />
            }
        </Switch>
          
         
        
          </div>
    </Router>      
      );
    }
    


//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@HOMEPAGE COMPONENT    
const Home = () => {
    

    
    
    
    const [occupation, setoccupation] = useState(); //these are the react states that hold the form information
    const [job_details,set_job_details] = useState({});
    const [location, setlocation] = useState();
    const [radius, setradius] = useState();
    const [salary, setsalary] = useState();
    const [ourform, setform] = useState([]);
    const [submitting, setSubmitting] = useState(false);//this is the bool that gets used after the user clicks submit. it sends a message to user.
    const [is_shown, set_is_shown] = useState(false);
    const handleSubmit = event => { //This function is called when the submit button is pressed. It creates a List from the form information and stores it in "ourform"
      event.preventDefault();
      setSubmitting(true);
      var list=[];
      list.push(occupation);
      list.push(location);
      list.push(radius);
      list.push(salary);
      setform(list);
      set_is_shown(true);
      searchJob(occupation, location, radius, salary);
      // console.log(Login.clientId)
      
      setTimeout(() => {
        setSubmitting(false);
      }, 3000);
    };
    
  function searchJob(occupation, location, radius, salary) {
      const url = BASE_URL + "/searchJob" + "?occupation=" + occupation + "&location=" + location + "&radius=" + radius + "&salary=" + salary;
      fetch(url, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json'
        },
      })
      .then(response => {
        return response.json();
      }).then(responseData => {
        console.log(responseData);
        let temp = [];
        temp = responseData;
        set_job_details(temp);
      });
    }
    let list;
    if (is_shown){
      list = <div className="dark-matter">
           <Jobs  details={job_details} job_number="0"/>
           <Jobs  details={job_details} job_number="1"/>
           <Jobs  details={job_details} job_number="2"/>
           <Jobs  details={job_details} job_number="3"/>
           <Jobs  details={job_details} job_number="4"/>
           </div>;
    }
    else{
      list = <div><p>Please Fill out the search form...</p></div>
    }

    return (
      <Fragment>
        <div className="mainform">
          <h1>JobFind</h1>
          {submitting &&
           <div>Searching jobs...</div>
          }
          <form onSubmit={handleSubmit}>
            <fieldset>
              <label>
                <div>Occupation: <input class="input_boxes" name="occupation" type='text' value={occupation} onChange={e => setoccupation(e.target.value)}/></div>
                <div>Location: <input class="input_boxes" name="location" type='text' value={location} onChange={e => setlocation(e.target.value)}/></div>
                <div>Radius: <input class="input_boxes" name="radius" type='text' value={radius} onChange={e => setradius(e.target.value)}/></div>
                <div>Salary: <input class="input_boxes" name="salary" type='text' value={salary} onChange={e => setsalary(e.target.value)}/></div>
              </label>
            </fieldset>
            <button class="button" type="submit">Submit</button>
          </form>
          <div>
           {list}
          </div>
            
      </div>
        
          
      </Fragment> 
);  
};


//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@APPLIED PAGE
const Applied = () => {
  const { idFavApplied } = useParams()
  const [favorited_list,set_favorited_list] = useState({});
  function getAppliedJob(id) {
    const url = BASE_URL + "/getAppliedJob" + "?id=" + id;
    fetch(url, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      },
    })
    .then(response => {
      return response.json();
    }).then(responseData => {
      console.log("this is from applied component:")
      console.log(responseData);
      

      //console.log(responseData);
      let temp = {};

      temp = responseData;
      set_favorited_list(temp);
      
    });
  }
  //var tempid="123321"
  getAppliedJob(idFavApplied);
  
  return (
  
  <Fragment>
    <h1>display "temp" dictionary here with favorites data </h1>

  </Fragment>
  );
};


const Favorites = () => {

  
  
  var fake_id = "123321";
  const { idFavApplied } = useParams();
  console.log(idFavApplied);
  const [favorited_list,set_favorited_list] = useState({});
  //getFavoritedjob(idFavApplied);
  let temp = [];
  
    console.log(idFavApplied);
    const url = BASE_URL + "/getfavJob" + "?id=" + idFavApplied;
    fetch(url, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      },
    })
    .then(response => {
      return response.json();
    }).then(responseData => {
      //console.log(responseData);
      
      temp = responseData;
      console.log(temp);
      //set_favorited_list(temp);
    });
    
    //set_favorited_list(temp);
  
  //console.log(temp);
  return (
  <div>
    <h1>display "temp" dictionary here with favorites data </h1>
  </div>
  );
};

/*###leaving this here as a skeleton for another possible page
const Contact = () => (
  <Fragment>
    <h1>Contact</h1>
  </Fragment>
  );
    
*/   

export default App;