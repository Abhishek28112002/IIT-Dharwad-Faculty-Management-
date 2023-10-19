import React, { Component } from 'react'
import { useNavigate } from 'react-router-dom';
const SignIn =()=>{
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    navigate('/Home');
    window.location.reload();
  };
    return (
      <div className='LandingPage'>
        <h3 className='Headin' style={{color:'#167bff'}}>IIT Dharwad Faculty Profile</h3>
      <form  style={{width:'400px'}} className='FormPage'>
       
        <h3>Sign In</h3>
        <div className="mb-3">
          <label>Email address</label>
          <input
            type="email"
            className="form-control"
            placeholder="Enter email"
          />
        </div>
        <div className="mb-3">
          <label>Password</label>
          <input
            type="password"
            className="form-control"
            placeholder="Enter password"
          />
        </div>
        
        <div className="d-grid" onClick={handleSubmit}>
          <button type="submit" className="btn btn-primary">
            Submit
          </button>
        </div>
        <p className="forgot-password text-right">
          Create new account <a href="/signUp">sign up?</a>
        </p>
      </form>
      </div>
    )
  }
export default SignIn;