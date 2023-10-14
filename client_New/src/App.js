import React from 'react';
import { Routes, Route, BrowserRouter } from 'react-router-dom'; // Use BrowserRouter
import Navbar from './Navbar';
import Home from './pages/Home';
import Research from './pages/Research';
import Publications from './pages/Publications';
import Contact from './pages/Contact';
import Profile from './pages/Profile';
function App() {
  return (
    <BrowserRouter>
      {/* Use BrowserRouter instead of Router */}
      <Navbar />
      <div className="container mt-3">
        <Routes>
          <Route path="/Research" element={<Research />} />
          <Route path="/Publications" element={<Publications />} />
          <Route path="/Contact" element={<Contact />} />
          <Route path="/Profile" element={<Profile />} />
          <Route path="/" element={<Home />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
