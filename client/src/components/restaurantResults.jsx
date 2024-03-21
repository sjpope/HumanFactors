import React from 'react';

const RestaurantList = () => {

  const restaurants = [
    { id: 1, name: 'Restaurant 1', cuisine: 'Italian', rating: 4.5 },
    { id: 2, name: 'Restaurant 2', cuisine: 'Mexican', rating: 4.2 },
    { id: 3, name: 'Restaurant 3', cuisine: 'Japanese', rating: 4.7 },
    { id: 4, name: 'Restaurant 4', cuisine: 'Indian', rating: 4.0 },
    { id: 5, name: 'Restaurant 5', cuisine: 'American', rating: 4.3 }
  ];

  return (
    <div className="restaurant-list-container">
      {restaurants.map(restaurant => (
        <div key={restaurant.id} className="restaurant-card-results">
          <h2>{restaurant.name}</h2>
          <p>Cuisine: {restaurant.cuisine}</p>
          <p>Rating: {restaurant.rating}</p>
        </div>
      ))}
    </div>
  );
};

export default RestaurantList;
