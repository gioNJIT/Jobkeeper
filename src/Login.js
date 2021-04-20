import { socket } from './App.js';
import React from 'react';

import { GoogleLogin } from 'react-google-login';


const clientId =
 process.env.REACT_APP_GOOGLE_API_KEY;

function Login() {
  const onSuccess = (res) => {
    console.log('Login Success: currentUser:', res.profileObj);
    socket.emit("UserLoggedIn")
  };

  const onFailure = (res) => {
    console.log('Login failed: res:', res);
    socket.emit("UserLoggedIn")
  };

  return (
    <div>
      <GoogleLogin
        clientId={clientId}
        buttonText="Login"
        onSuccess={onSuccess}
        onFailure={onFailure}
        //cookiePolicy={'single_host_origin'}
        style={{ marginTop: '100px' }}
        isSignedIn={true}
      />
    </div>
  );
}

export default Login;