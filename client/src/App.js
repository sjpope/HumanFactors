import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import HomePage from './pages/HomePage';
import ResultsPage from './pages/ResultsPage'

// React Router setup
function App() {
  // Note: use console.log for React logging
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/results" element={< ResultsPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
