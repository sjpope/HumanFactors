import React, { useState, useEffect } from 'react';
import { Navigate, useNavigate } from 'react-router-dom';
import './Profile.css';

function Profile() {
    const [user, setUser] = useState(null);
    const [profilePicture, setProfilePicture] = useState(null);
    const [diningPreferences, setDiningPreferences] = useState('');
    const [allergies, setAllergies] = useState('');
    const [favoriteCuisines, setFavoriteCuisines] = useState('');
    const [desiredExperiences, setDesiredExperiences] = useState('');
    const [upcomingReservations, setUpcomingReservations] = useState([]);
    const [profileUpdated, setProfileUpdated] = useState(false);
    const navigate = useNavigate();

    useEffect(() => {
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
            setAllergies(data.allergies);
            setFavoriteCuisines(data.favorite_cuisines);
            setDesiredExperiences(data.desired_dining_experiences);
            setUpcomingReservations(data.upcoming_reservations || []);
        })
        .catch(error => console.error('Error fetching profile:', error));
    }, [profileUpdated]);

    if (!localStorage.getItem('token')) {
        return <Navigate to="/login" />;
    }

    const handlePictureChange = (event) => {
        setProfilePicture(event.target.files[0]);
    };

    const handleDiningPreferencesChange = (event) => {
        setDiningPreferences(event.target.value);
    };

    const handleAllergiesChange = (event) => {
        setAllergies(event.target.value);
    };

    const handleFavoriteCuisinesChange = (event) => {
        setFavoriteCuisines(event.target.value);
    };

    const handleDesiredExperiencesChange = (event) => {
        setDesiredExperiences(event.target.value);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        const formData = new FormData();
        formData.append('profile_picture', profilePicture);
        formData.append('dining_preferences', diningPreferences);
        formData.append('allergies', allergies);
        formData.append('favorite_cuisines', favoriteCuisines);
        formData.append('desired_dining_experiences', desiredExperiences);

        const token = localStorage.getItem('token');
        fetch('http://127.0.0.1:8000/api/profile/', {
            method: 'PUT',
            headers: {
                'Authorization': `Token ${token}`,
            },
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            console.log('Profile updated:', data);
            setProfileUpdated(true); // Trigger re-fetch of user data
        })
        .catch(error => console.error('Failed to update profile:', error));
    };

    const goToRestaurants = () => {
        navigate('/');
    };

    return (
        <div className="profile-page">
            <h1>Profile</h1>
            <form onSubmit={handleSubmit} className="profile-form">
                <div className="form-group">
                    <label>Username:</label>
                    <input type="text" value={user?.username ?? ''} disabled />
                </div>
                <div class="form-group">
                    <label>Email:</label>
                    <input type="email" value={user?.email ?? ''} disabled />
                </div>
                <div className="form-group">
                    <label>Profile Picture:</label>
                    <input type="file" onChange={handlePictureChange} />
                </div>
                <div className="form-group">
                    <label>Dining Preferences:</label>
                    <textarea value={diningPreferences} onChange={handleDiningPreferencesChange} />
                </div>
                <div className="form-group">
                    <label>Allergies:</label>
                    <textarea value={allergies} onChange={handleAllergiesChange} />
                </div>
                <div className="form-group">
                    <label>Favorite Cuisines:</label>
                    <textarea value={favoriteCuisines} onChange={handleFavoriteCuisinesChange} />
                </div>
                <div className="form-group">
                    <label>Desired Dining Experiences:</label>
                    <textarea value={desiredExperiences} onChange={handleDesiredExperiencesChange} />
                </div>
                <button type="submit">Update Profile</button>
            </form>

            <div>
                <h2>Upcoming Reservations</h2>
                <ul>
                    {upcomingReservations.length > 0 ? (
                        upcomingReservations.map(reservation => (
                            <li key={reservation.id}>
                                <p><strong>Restaurant:</strong> {reservation.restaurant_name}</p>
                                <p><strong>Date & Time:</strong> {reservation.date_time}</p>
                            </li>
                        ))
                    ) : (
                        <p>No upcoming reservations found.</p>
                    )}
                </ul>
            </div>

            <button className="home-button" onClick={goToRestaurants}>Return to Home</button>
        </div>
    );
}

export default Profile;
