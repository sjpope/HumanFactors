import React, { useState, useEffect } from 'react';
import '../App.css';
import Header from '../components/header';
import SearchBar from '../components/searchBar';
import RestaurantCard from '../components/restaurantCard';
import Footer from '../components/footer';

function HomePage() {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/home/')  
      .then(response => response.json())
      .then(data => {
        setRestaurants(data);
      })
      .catch(error => {
        console.error('Error fetching data: ', error);
      });
  }, []);

  return (
    <div>
      <Header />
      <SearchBar />
      <div className="restaurant-cards-container">
        {restaurants.map((restaurant, index) => (
          <RestaurantCard key={index} name={restaurant.name} />
        ))}
      </div>
      <Footer />
    </div>
  );
}

export default HomePage;
