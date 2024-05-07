import React, { useState, useEffect } from 'react';

function ReviewList({ restaurantId }) {
    const [reviews, setReviews] = useState([]);

    useEffect(() => {
        fetch(`http://127.0.0.1:8000/api/restaurant/${restaurantId}/reviews/`)
            .then(response => response.json())
            .then(data => setReviews(data))
            .catch(error => console.error('Error fetching reviews:', error));
    }, [restaurantId]);

    return (
        <div>
            <h3>Reviews</h3>
            {reviews.length ? (
                <ul>
                    {reviews.map(review => (
                        <li key={review.id}>
                            <p>{review.title}</p>
                            <p>{review.description}</p>
                            <p>Rating: {review.rating}</p>
                        </li>
                    ))}
                </ul>
            ) : <p>No reviews yet.</p>}
        </div>
    );
}

export default ReviewList;
