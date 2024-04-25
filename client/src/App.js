import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import HomePage from './pages/HomePage';
import ResultsPage from './pages/ResultsPage';
import Login from './pages/Login';
import Logout from './pages/Logout';
import Register from './pages/Register';
import Profile from './pages/Profile';
import { Navigate } from 'react-router-dom';

// React Router setup
function App() {
  const isAuthenticated = localStorage.getItem('token');
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/results" element={<ResultsPage />} />
          <Route path="/login" element={<Login />} />
          <Route path="/logout" element={<Logout />} />
          <Route path="/register" element={<Register />} />
          <Route
            path="/profile"
            element={isAuthenticated ? <Profile /> : <Navigate to="/login" />}
          />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
