import React, { useState, useEffect } from 'react';
import ReviewList from './ReviewPage';  // Assuming you have a component to list reviews
import Reservation from './Reservation';  // Assuming you have a component to make reservations
import { useParams } from 'react-router-dom';
import './RestaurantDetail.css';

function RestaurantDetail({ restaurantId }) {
    const { id } = useParams(); // Get the restaurant id from the URL
    const [restaurant, setRestaurant] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetch(`http://127.0.0.1:8000/api/restaurant/${id}/`)
            .then(response => response.json())
            .then(data => {
                setRestaurant(data);
                setLoading(false);
            })
            .catch(error => {
                console.error('Error fetching restaurant details:', error);
                setLoading(false);
            });
    }, [id]);

    if (loading) return <p>Loading...</p>;
    if (!restaurant) return <p>No data available for this restaurant.</p>;

    return (
        <div className="restaurant-detail">
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
