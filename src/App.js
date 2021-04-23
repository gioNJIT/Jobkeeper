import React, { Fragment } from "react";
import './App.css';
import Login from './Login';
import { ListItem } from './ListItem';
import  { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Link, Switch, useParams, Redirect } from "react-router-dom";

const BASE_URL = "/api/v1/job"




function App() {

   
    const jobDataTest = "this is a job posting"; //this is mocking the job posting data that will be passed to the components
    const [isAuthenticated, setIsAuthenticated] = useState(true); //thi is mocking the login authentication. change to false to test
    
    
  
  

  
  
  console.log(isAuthenticated);
  
  return (
    <Router>  
        <div>
        <nav>
            <Link to="/Home">Home</Link>|
            <Link to={`/about/${jobDataTest}`}>About</Link>|
            <Link to="/Login">Login</Link>|
            <Link to="/Favorites">Favorites</Link>
        </nav>
        <Switch>
            <Route path="/Login"  component={Login} />
            {
            isAuthenticated ? 
            <>
            <Redirect to="/Home" />
            <Route path="/Home" component={Home} />
            <Route path="/about/:jobDataTest"  component={About} />
            <Route path="/Favorites"  component={Favorites} />
            </> : <Redirect to="/Login" />
            }
      
            
        </Switch>
          
         
        
          </div>
    </Router>      
      );
    }
    


//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@HOMEPAGE COMPONENT    
const Home = () => {

    const [occupation, setoccupation] = useState(); //these are the react states that hold the form information
    const [job_details,set_job_details] = useState([]);
    const [location, setlocation] = useState();
    const [radius, setradius] = useState();
    const [salary, setsalary] = useState();
    const [ourform, setform] = useState([]);
    const [submitting, setSubmitting] = useState(false); //this is the bool that gets used after the user clicks submit. it sends a message to user.
    const isLogedIn = true;
    const handleSubmit = event => { //This function is called when the submit button is pressed. It creates a List from the form information and stores it in "ourform"
      event.preventDefault();
      setSubmitting(true);
      var list=[];
      list.push(occupation);
      list.push(location);
      list.push(radius);
      list.push(salary);
      setform(list);
      
      searchJob(occupation, location, radius, salary);

      
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
        
      }).then(responseData => {
        console.log(responseData);
      });
    }

    return (
      <Fragment>
        <div className="mainform">
          <h1>Job search</h1>
          {submitting &&
           <div>Searching jobs...</div>
          }
          <form onSubmit={handleSubmit}>
            <fieldset>
              <label>
                <div>Occupation: <input name="occupation" type='text' value={occupation} onChange={e => setoccupation(e.target.value)}/></div>
                <div>Location: <input name="location" type='text' value={location} onChange={e => setlocation(e.target.value)}/></div>
                <div>Radius: <input name="radius" type='text' value={radius} onChange={e => setradius(e.target.value)}/></div>
                <div>Salary: <input name="salary" type='text' value={salary} onChange={e => setsalary(e.target.value)}/></div>
              </label>
            </fieldset>
            <button type="submit">Submit</button>
          </form>
          <div>
            <p> Hello there </p>
           { job_details.map((item, index) => <ListItem key={index} name={item} />)}
          </div>
            
      </div>
        
          
      </Fragment> 
);  
};


//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@TESTING PAGE COMPONENT. DELETE WHILE FINALIZING
const About = () => {
  const { jobDataTest } = useParams()
  return (
  <Fragment>
    
    <h1>{ jobDataTest }</h1>
    
  </Fragment>
)
};


const Favorites = () => (
  <Fragment>
    <h1>favorites has to pull directly from database</h1>
    <h2>interaction with the other pages is not needed so sending components here is unneccesary</h2>
  </Fragment>
  );

/*###leaving this here as a skeleton for another possible page
const Contact = () => (
  <Fragment>
    <h1>Contact</h1>
  </Fragment>
  );
    
*/   

export default App;