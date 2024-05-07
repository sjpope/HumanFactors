import React, { useState, useEffect } from 'react';
import { Navigate } from 'react-router-dom';

function Profile() {
    const [user, setUser] = useState(null);
    const [profilePicture, setProfilePicture] = useState(null);
    const [diningPreferences, setDiningPreferences] = useState('');
    const [upcomingReservations, setUpcomingReservations] = useState([]);

    useEffect(() => {
        // Fetch user data from the backend
        const token = localStorage.getItem('token');
        fetch('http://127.0.0.1:8000/api/profile/', {
            headers: {
                'Authorization': `Token ${token}`,
            },
        })
        .then(response => response.json())
        .then(data => {
            setUser(data);
            setDiningPreferences(data.dining_preferences);
            // Ensure upcomingReservations is initialized as an empty array
            setUpcomingReservations(data.upcoming_reservations || []);
        })
        .catch(error => console.error('Error fetching profile:', error));
    }, []);

    if (!localStorage.getItem('token')) {
        return <Navigate to="/login" />;
    }

    const handlePictureChange = (event) => {
        setProfilePicture(event.target.files[0]);
    };

    const handlePreferencesChange = (event) => {
        setDiningPreferences(event.target.value);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        const formData = new FormData();
        formData.append('profile_picture', profilePicture);
        formData.append('dining_preferences', diningPreferences);

        const token = localStorage.getItem('token');
        fetch('http://127.0.0.1:8000/api/profile/', {
            method: 'PUT',
            headers: {
                'Authorization': `Token ${token}`,
            },
            body: formData
        })
        .then(response => response.json())
        .then(data => console.log('Profile updated:', data))
        .catch(error => console.error('Failed to update profile:', error));
    };


    return (
        <div>
            <h1>Profile</h1>
            <form onSubmit={handleSubmit}>
                {/* Display user information and include form elements for the profile picture and dining preferences */}
                <label>
                    Username:
                    <input type="text" value={user?.username} disabled />
                </label>
                <label>
                    Email:
                    <input type="email" value={user?.email} disabled />
                </label>
                <label>
                    Profile Picture:
                    <input type="file" onChange={handlePictureChange} />
                </label>

                <label>
                    Dining Preferences:
                    <textarea value={diningPreferences} onChange={handlePreferencesChange} />
                </label>
                <button type="submit">Update Profile</button>

            </form>

            <div>
                <h2>Upcoming Reservations</h2>
                <ul>
                    {upcomingReservations.map(reservation => (
                        <li key={reservation.id}>
                            {/* Display reservation details */}
                            <p>{reservation.restaurant_name}</p>
                            <p>{reservation.date_time}</p>
                        </li>
                    ))}
                </ul>
            </div>

        </div>
    );
}

export default Profile;
