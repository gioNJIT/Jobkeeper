import React from "react";
import './App.css';
import  { useState, useEffect } from 'react';
const BASE_URL = "/api/v1/job";


export function Appliedfunct (props){
    var { id } = props;
    const [appl_list, set_appl_list] = useState([]);
    console.log("testttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt"); 
    function getAppliedjob(id) {
    const url = BASE_URL +
    "/getAppliedJob" +
    "?id=" +
    id;
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
      let temp = {};
      temp = responseData;
      set_appl_list(temp);
      
    });
  }
  console.log(appl_list);
  
  
   useEffect(() => {
    getAppliedjob(id);
  }, [id]);
    return (
  <div>
  <ul>
    { appl_list.map((item, index) => (
        <div className="single_entry" >
        <ul> Title: {item[1]}</ul>
        <ul> Location : {item[2]}</ul>
        <ul> Salary : {item[3]}</ul>
        <ul> Id : {item[0]}</ul>
        <ul> Link: <a href={item[4]}>Take me to the job</a></ul>
        </div>
    )
    )}
   </ul>
  </div>
  );
    
}
export default Appliedfunct;