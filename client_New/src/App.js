import React, { useEffect, useState } from "react";
import { useNavigate, Routes, Route, BrowserRouter, Navigate } from 'react-router-dom';

import Navbar from "./Navbar";
import Home from "./pages/Home";
import Research from "./pages/Research";
import Publications from "./pages/Publications";
import Contact from "./pages/Contact";
import Profile from "./pages/Profile";
import Login from "./pages/Login";
import SignUp from "./pages/SignUp";
import { GetItemLocalStorage } from "./Services";

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(true);
  const[PathName,setPathName]=useState('/home')
  useEffect( () => {
    setPathName(window.location.pathname)
  },[]);

  useEffect(() => {
    // const userData = GetItemLocalStorage('user');
    // if (userData) {
    //   setIsAuthenticated(true);
    // } else {
    //   setIsAuthenticated(false);
    // }
  }, []);



  return (
    <BrowserRouter>
     { PathName!='/signIn' && PathName!='/signUp'&& PathName!='/' && <Navbar />}
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/signIn" element={<Login />} />
        <Route path="/signUp" element={<SignUp />} />
        <Route
          path="/Research"
          element={isAuthenticated ? <Research /> : <Navigate to="/signIn" replace />}
        />
        <Route
          path="/Publications"
          element={isAuthenticated ? <Publications /> : <Navigate to="/signIn" replace />}
        />
        <Route path="/Profile" element={isAuthenticated ? <Profile /> : <Navigate to="/signIn" replace />} />
        <Route path="/Profile/:id" element={isAuthenticated ? <Profile /> : <Navigate to="/signIn" replace />} />
        <Route path="/Home" element={isAuthenticated ? <Home /> : <Navigate to="/signIn" replace />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
