// components/RestaurantList.js
import React from 'react';
import { Link } from 'react-router-dom';
import './RestaurantList.css';

function RestaurantList({ restaurants }) {
    return (
        <div className="restaurant-list">
            {restaurants.length > 0 ? (
                restaurants.map((restaurant, index) => (
                    <Link to={`/restaurant/${restaurant.id}`} key={index} className="restaurant-link">
                        <div className="restaurant-list-item">
                            <h3>{restaurant.name}</h3>
                            <p>{`Cuisine: ${restaurant.cuisine_type}`}</p>
                        </div>
                    </Link>
                ))
            ) : (
                <p>No results found.</p>
            )}
        </div>
    );
}

export default RestaurantList;
