// components/RestaurantCard.js
import React from 'react';
import './RestaurantCard.css';

function RestaurantCard({ name, cuisine }) {
    return (
        <div className="restaurant-card">
            <h3>{name}</h3>
            <p>{`Cuisine: ${cuisine}`}</p>
        </div>
    );
}

export default RestaurantCard;
