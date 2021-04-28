import React from 'react';

import { GoogleLogout } from 'react-google-login';


const clientId =
 process.env.REACT_APP_GOOGLE_API_KEY;
 
 function Logout() {
  const onSuccess = (res) => {
    alert('You Logout ');
  };
  
  
return (
    <div>
      <GoogleLogout
        clientId={clientId}
        buttonText="Logout"
        onLogoutSuccess={onSuccess}
       ></GoogleLogout>
    </div>
  );
}

export default Logout;
