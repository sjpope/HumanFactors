import React, { useState, useEffect } from 'react';
import ReviewList from './ReviewList';  // Assuming you have a component to list reviews

function RestaurantDetail({ restaurantId }) {
    const [restaurant, setRestaurant] = useState(null);

    useEffect(() => {
        fetch(`http://127.0.0.1:8000/api/restaurant/${restaurantId}/`)
            .then(response => response.json())
            .then(data => setRestaurant(data))
            .catch(error => console.error('Error fetching restaurant details:', error));
    }, [restaurantId]);

    if (!restaurant) return <p>Loading...</p>;

    return (
        <div>
            <h2>{restaurant.name}</h2>
            <p>{restaurant.address}</p>
            <p>{`Cuisine: ${restaurant.cuisine_type}`}</p>
            <p>{`Health Rating: ${restaurant.health_rating}`}</p>
            <p>{`Price Level: ${restaurant.price_level}`}</p>
            <ReviewList restaurantId={restaurantId} />
            <Reservation restaurantId={restaurantId} />
        </div>
    );
}

export default RestaurantDetail;
