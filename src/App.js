import React from 'react';
import './App.css';
import Login from './Login';
import  { useState } from 'react';


function App() {
    {/*
  const [occupation, setoccupation] = useState(); //these are the react states that hold the form information
  const [location, setlocation] = useState();
  const [radius, setradius] = useState();
  const [salary, setsalary] = useState();
  const [ourform, setform] = useState([]);
  const [submitting, setSubmitting] = useState(false); //this is the bool that gets used after the user clicks submit. it sends a message to user.
  const isLogedIn = false;
  const handleSubmit = event => { //This function is called when the submit button is pressed. It creates a List from the form information and stores it in "ourform"
    event.preventDefault();
   setSubmitting(true);
   var list=[];
   list.push(occupation);
   list.push(location);
   list.push(radius);
   list.push(salary);
   setform(list);

   setTimeout(() => {
     setSubmitting(false);
   }, 3000);
 };

  */}
  
  
  
  
  return (
    <div>
      <Login />
     {/*
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
      {ourform.map((objects) => (
          objects
        ))}
    </div>*/}
      </div>
  );
}
    
    

export default App;