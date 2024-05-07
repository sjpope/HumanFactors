import React from 'react';

function Logout() {
    const handleLogout = () => {
        fetch('http://127.0.0.1:8000/api/logout/', {
            method: 'POST',
            headers: {
                'Authorization': `Token ${localStorage.getItem('token')}`,
                'Content-Type': 'application/json',
            },
        })
        .then(() => {
            localStorage.removeItem('token');
            window.location.href = "/login";  // Redirect to login on logout
        });
    };

    return (
        <button onClick={handleLogout} className="logout-button">Logout</button>
    );
}

export default Logout;
