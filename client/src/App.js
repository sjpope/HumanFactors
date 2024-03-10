import React from 'react';
import './App.css';
import Header from './components/header';
import SearchBar from './components/searchBar';
import RestaurantCard from './components/restaurantCard';

function App() {
  const restaurants = [
    { name: 'Restaurant 1' },
    { name: 'Restaurant 2' },
    { name: 'Restaurant 3' },
    { name: 'Restaurant 4' },
    { name: 'Restaurant 5' }
  ];

  return (
    <div>
      <Header />
      <SearchBar />
      <div className="restaurant-cards-container">
        {restaurants.map((restaurant, index) => (
          <RestaurantCard key={index} name={restaurant.name} />
        ))}
      </div>
    </div>
  );
}

export default App;
