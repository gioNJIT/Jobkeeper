import React, { Fragment } from "react";
import './App.css';
import Login from './Login';
import Logout from './Logout';
import { ListItem } from './ListItem';
import  { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Link, Switch, useParams, Redirect } from "react-router-dom";
import PropTypes from 'prop-types';

export function Jobs(props){
    const { google_id } = props;
    const { details } = props;
    const {job_number} = props;
    const test = props.details[0];
    const BASE_URL = "/api/v1/job";
    const [job_info, set_job_info] = useState({});
    const [title, set_title] = useState([]);
    const [empty, set_empty] = useState(false);
    const [realID, set_realID] = useState('');
    
    console.log(google_id);
    
    //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@This function sends FAVORITED data to backend
  function sendFavoritedDataToServer(mainID, jobTitle, jobLocation, jobSalary, jobId, jobLink) {
  const url = BASE_URL + "/Favorites";
  var data = JSON.stringify({
    "user_id": mainID,
    "title":jobTitle,
    "location":jobLocation,
    "salary" : jobSalary,
    "id" : jobId,
    "link" : jobLink
      
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
    
    

    //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@This function sends APPLIED data to backend
  function sendAppliedDataToServer(mainID, jobTitle, jobLocation, jobSalary, jobId, jobLink) {
  const url = BASE_URL + "/Applied";
  var data = JSON.stringify({
    "user_id": mainID,
    "title":jobTitle,
    "location":jobLocation,
    "salary" : jobSalary,
    "id" : jobId,
    "link" : jobLink
      
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


   



//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@FAVORITES FUNCTION    
    function Favourits(props){
        //console.log(job_info);
        //console.log(job_number);
        console.log(details[job_number]);
        console.log("Added to the favourtie");
        
        sendFavoritedDataToServer(realID, title[0], title[1], title[2], title[3], title[4])
    }


//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@APPLIED FUNCTION     
     function Appliedfunc(props){
        //console.log(job_info);
        //console.log(job_number);
        console.log(details[job_number]);
        console.log("Added to the applied list");
        
        sendAppliedDataToServer(realID, title[0], title[1], title[2], title[3], title[4])
        
    }
    
    
    
    
    
    useEffect(() => {
  set_job_info(details);
  let title_name ;
  title_name= details[job_number];
  set_title(title_name);
  set_realID(google_id);
  set_empty(true);
  }, [details]);
  
  if(!!title){  
  return (
    <div className="single_entry">
      <center>
     <pre>
     <p>
      Title: 
      {title[0]}
      </p>
      <p>
      Location: 
      {title[1]}
      </p>
      <p>
      Salary: 
      {title[2]}
      </p>
      <p>
      Link: 
      <a href={title[4]}>Take me to the job</a>
      </p>
     </pre>
     
      <button type="button" className="button" onClick={Favourits}> Add To Favorites List </button>
      <button type="button" className="button" onClick={Appliedfunc}> Add To Applied List </button>
      </center>
    </div>
  );
    
  }
    return null;
  
    
    
    
}

export default Jobs;