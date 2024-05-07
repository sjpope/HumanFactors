import React, { useState, useEffect } from 'react';
import ReviewList from './ReviewPage';  // Assuming you have a component to list reviews
import Reservation from './Reservation';  // Assuming you have a component to make reservations
import { useParams } from 'react-router-dom';
import './RestaurantDetail.css';

function RestaurantDetail({ restaurantId }) {
    const { id } = useParams(); // Get the restaurant id from the URL
    const [restaurant, setRestaurant] = useState(null);
    const [loading, setLoading] = useState(true);
    const [dateTime, setDateTime] = useState('');
    const [review, setReview] = useState({ rating: '', text: '' });
    const [message, setMessage] = useState('');
    
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
    const handleReservation = (e) => {
        e.preventDefault();
        fetch(`http://127.0.0.1:8000/api/restaurant/${id}/book/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ date_time: dateTime }),
        })
            .then(response => response.json())
            .then(data => setMessage(data.status || 'Failed to book a reservation'))
            .catch(error => setMessage(`Error: ${error.message}`));
    };

    const handleReviewSubmit = (e) => {
        e.preventDefault();
        fetch(`http://127.0.0.1:8000/api/restaurant/${id}/reviews/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                rating: review.rating,
                description: review.text,
            }),
        })
            .then(response => response.json())
            .then(data => setMessage(data.status || 'Failed to submit review'))
            .catch(error => setMessage(`Error: ${error.message}`));
    };

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
            {/* <Reservation restaurantId={restaurantId} /> */}

            {/* Reservation Form */}
            <div className="reservation-form">
                <h3>Book a Reservation</h3>
                <form onSubmit={handleReservation}>
                    <label>
                        Date and Time:
                        <input
                            type="datetime-local"
                            value={dateTime}
                            onChange={(e) => setDateTime(e.target.value)}
                            required
                        />
                    </label>
                    <button type="submit">Book Reservation</button>
                </form>
            </div>

            {/* Review Form */}
            <div className="review-form">
                <h3>Leave a Review</h3>
                <form onSubmit={handleReviewSubmit}>
                    <label>
                        Rating:
                        <input
                            type="number"
                            min="1"
                            max="5"
                            value={review.rating}
                            onChange={(e) => setReview({ ...review, rating: e.target.value })}
                            required
                        />
                    </label>
                    <label>
                        Review:
                        <textarea
                            value={review.text}
                            onChange={(e) => setReview({ ...review, text: e.target.value })}
                            required
                        />
                    </label>
                    <button type="submit">Submit Review</button>
                </form>
            </div>

            {/* Message Display */}
            {message && <p>{message}</p>}
        </div>
    );
}

export default RestaurantDetail;

