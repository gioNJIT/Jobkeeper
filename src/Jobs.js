import React, { Fragment } from "react";
import './App.css';
import Login from './Login';
import Logout from './Logout';
import { ListItem } from './ListItem';
import  { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Link, Switch, useParams, Redirect } from "react-router-dom";
import PropTypes from 'prop-types';

export function Jobs(){
    //const [job_list, set_job_list] = useState(['', '', '', '', '', '', '', '', '']);
    //const { name } = props;
    //console.log(name);
    console.log("That worked....");
    return <div><p>Hello world</p></div>;
    
    
}

export default Jobs;