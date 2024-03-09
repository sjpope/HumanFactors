import React from 'react';

const RestaurantCard = ({ name }) => {
  return (
    <div className="restaurant-card">
      <h3>{name}</h3>
    </div>
  );
};

export default RestaurantCard;
