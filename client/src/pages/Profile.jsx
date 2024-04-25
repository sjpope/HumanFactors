import React, { useState, useEffect } from 'react';
import { Navigate } from 'react-router-dom';

function Profile() {
    const [user, setUser] = useState(null);
    const [profilePicture, setProfilePicture] = useState(null);
    const [diningPreferences, setDiningPreferences] = useState('');

    useEffect(() => {
        // TODO: Fetch user data from the backend and set it in state
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

    const handleSubmit = (event) => {
        event.preventDefault();
        // TODO: Implement the logic to submit the form and update the user profile
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
        </div>
    );
}

export default Profile;
