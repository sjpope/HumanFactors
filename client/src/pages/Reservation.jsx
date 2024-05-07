import React, { useState } from 'react';

function Reservation({ restaurantId }) {
    const [dateTime, setDateTime] = useState('');
    const [success, setSuccess] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault();
        fetch(`http://127.0.0.1:8000/api/restaurant/${restaurantId}/book/`, {
            method: 'POST',
            headers: {
                'Authorization': `Token ${localStorage.getItem('token')}`,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ date_time: dateTime })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to book reservation');
            }
            return response.json();
        })
        .then(data => {
            setSuccess('Reservation booked successfully!');
            setError('');
        })
        .catch(error => {
            setError(error.message);
            setSuccess('');
        });
    };

    return (
        <div>
            <h3>Book a Reservation</h3>
            <form onSubmit={handleSubmit}>
                <label>
                    Choose your reservation date and time:
                    <input type="datetime-local" value={dateTime} onChange={e => setDateTime(e.target.value)} required />
                </label>
                <button type="submit">Book Reservation</button>
            </form>
            {success && <p style={{ color: 'green' }}>{success}</p>}
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
}

export default Reservation;
