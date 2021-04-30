import React, { Fragment } from "react";
import './App.css';
import Login from './Login';
import Logout from './Logout';
import { ListItem } from './ListItem';
import  { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Link, Switch, useParams, Redirect } from "react-router-dom";
import PropTypes from 'prop-types';

export function Jobs(props){
    const { details } = props;
    const {job_number} = props;
    const test = props.details[0];
    const BASE_URL = "/api/v1/job";
    const [job_info, set_job_info] = useState({details});
    const [empty, set_empty] = useState(false);
    
    
    
    
    
    
    function Favourits(props){
        console.log(job_info);
        console.log(job_number);
        console.log("Added to the favourtie");
        
        const url = BASE_URL + "/Favorites" + "?favorite=" + details[job_number];
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
        
        //set_job_details(responseData[0]);
      });
    }
    
    useEffect(() => {
  set_job_info(details[job_number]);
  set_empty(true);
  }, [details]);
  
  if(empty){  
  return (
    <div className="single_entry">
     <pre>
      Title: 
      {job_info}
     </pre>
      <button type="button" className="button" onClick={Favourits}> Add To Favorites </button>
    </div>
  );
    
  }
    return <div><p>Loading...</p></div>;
  
    
    
    
}

export default Jobs;