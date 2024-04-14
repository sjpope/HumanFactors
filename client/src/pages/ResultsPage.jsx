import React, { useState, useEffect } from 'react';
import '../App.css';
import Header from '../components/header';
import SideBar from '../components/sideBar';
import RestaurantList from '../components/restaurantResults';

function ResultsPage() {
  const [searchResults, setSearchResults] = useState([]);
  const searchQuery = '';   // From search component's state

  useEffect(() => {
    fetch('http://127.0.0.1:8000/home/search/?q=' + encodeURIComponent(searchQuery))
      .then(response => response.json())
      .then(data => {
        setSearchResults(data);
      })
      .catch(error => {
        console.error('Error fetching data: ', error);
      });
  }, [searchQuery]); 

  return (
    <div>
      <Header />
      <SideBar />
      <RestaurantList restaurants={searchResults} />
    </div>
  );
}

export default ResultsPage;
