import React from "react";
import './App.css';
import  { useState, useEffect } from 'react';

export function Jobs(props){
    const { details } = props;
    const {job_number} = props;
    //const test = props.details[0];
    const BASE_URL = "/api/v1/job";
    /* eslint-disable */
    const [job_info, set_job_info] = useState({});
    /* eslint-disable */
    const [title, set_title] = useState([]);
    const [empty, set_empty] = useState(false);
    
    
    
    //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@This function sends FAVORITED data to backend
  function sendFavoritedDataToServer(jobTitle, jobLocation, jobSalary, jobId, jobLink) {
  const url = BASE_URL + "/Favorites";
  var data = JSON.stringify({
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
  function sendAppliedDataToServer(jobTitle, jobLocation, jobSalary, jobId, jobLink) {
  const url = BASE_URL + "/Applied";
  var data = JSON.stringify({
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
        
        sendFavoritedDataToServer(title[0], title[1], title[2], title[3], title[4])
    }


//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@APPLIED FUNCTION     
     function Appliedfunc(props){
        //console.log(job_info);
        //console.log(job_number);
        console.log(details[job_number]);
        console.log("Added to the applied list");
        
        sendAppliedDataToServer(title[0], title[1], title[2], title[3], title[4])
        
    }
    
    
    
    
    
    useEffect(() => {
  set_job_info(details);
  let title_name ;
  title_name= details[job_number];
  set_title(title_name);
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
      <button type="button" className="button2" onClick={Appliedfunc}> Add To Applied List </button>
      </center>
    </div>
  );
    
  }
    return null;
  
    
    
    
}

export default Jobs;