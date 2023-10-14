import React, { useEffect, useState } from "react";
import { Routes, Route, BrowserRouter } from "react-router-dom"; // Use BrowserRouter
import Navbar from "./Navbar";
import Home from "./pages/Home";
import Research from "./pages/Research";
import Publications from "./pages/Publications";
import Contact from "./pages/Contact";
import Profile from "./pages/Profile";
import Login from "./pages/Login";
import SignUp from "./pages/SignUp";

function App() {
  const[PathName,setPathName]=useState('/home')
  useEffect( () => {
    setPathName(window.location.pathname)
  },[]);
  return (
    <BrowserRouter>
     { PathName!='/signIn' && PathName!='/signUp'&& PathName!='/' && <Navbar />}
     
        <Routes>
          <Route exact path="/" element={<Login />} />
          <Route path="/signIn" element={<Login />} />
          <Route path="/signUp" element={<SignUp />} />
          <Route path="/Research" element={<Research />} />
          <Route path="/Publications" element={<Publications />} />
          <Route path="/Contact" element={<Contact />} />
          <Route path="/Profile" element={<Profile />} />
          <Route path="/Home" element={<Home />} />
        </Routes>
     
    </BrowserRouter>
  );
}

export default App;