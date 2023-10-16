import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <div className="container">
        <Link to="/Home" className="navbar-brand" style={{ display: 'flex', gap: '8px' }}>
          <img
            src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAaCAMAAADhRa4NAAAAP1BMVEVHcEwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC6E+JdAAAAFXRSTlMATl0OLf8YItgofYzJ57U5oUQGcGhgoUpoAAABI0lEQVR4AY3PB4LEIAgF0A8KGI2jRO9/1k2yffqzd8EVYjwUIgARAFFxj0laskixJPH+DSIrasVFxHBXkgJVZEm4pWtNgAJntdbVbo9LAxaRCES5d4lIxfH+BagiuNKzIkkNLkJbkoQw+nUElXyVYpZlJU8iij/yGJN7Mpw0deYxMn6R7NIojB2XucqO8QePvN9RigOtnPLEHwHYWq5p+obZZZ0RgOJGTEJFLgGPTZGIxwKwbOHs3NJWWh+eW89jFDVc24IGsxCCRtO9+b32sJ2wpy/hrA44BDMnXZiYiLSpLUEXs99btPQyZ8kljz459zK8c+kNb9mmMxmTj8bmNJzdqXnk7M2JAuDupM1bc1dXo7bz4S3yQk4blkM86z8d+5n4AFnmDsTLM5lkAAAAAElFTkSuQmCC"
            alt="IIT Dharwad Logo"
          />
          IIT Dharwad
        </Link>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav" style={{display:'flex',alignItems:'center',justifyContent:'space-between'}}>
          <ul className="navbar-nav ml-auto"> {/* Add 'ml-auto' to align items to the right */}
            <li className="nav-item">
              <Link to="/Research" className="nav-link">
                Research
              </Link>
            </li>
            <li className="nav-item">
              <Link to="/Publications" className="nav-link">
                Publications
              </Link>
            </li>
            {/* <li className="nav-item">
              <Link to="/Contact" className="nav-link">
                Contact Us
              </Link>
            </li> */}
          </ul>
         
              <Link to="/Profile" className="nav-link">
               <img style={{width: '48px',borderRadius: '48px',height:'48px'}} src="data:image/jpeg;base64,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"></img>
              </Link>
           
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
