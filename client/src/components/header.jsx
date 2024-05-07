// header.jsx
import React from 'react';
import { useNavigate } from 'react-router-dom';

function Header() {
    const isAuthenticated = localStorage.getItem('token');
    const navigate = useNavigate();

    const handleRegister = (e) => {
        e.preventDefault();
        navigate('/register'); // Updated to use the client-side path for register
    };

    const handleLogin = (e) => {
        e.preventDefault();
        navigate('/login'); // Updated to use the client-side path for login
    };

    const handleLogout = (e) => {
        e.preventDefault();
        navigate('/logout'); // Updated to use the client-side path for login
    };
    const profilePage = (e) => {
        e.preventDefault();
        navigate('/profile');
    };

    return (
        <header>
            <h1>EasyBook</h1>
            <nav>
                {isAuthenticated && <button onClick={profilePage}>Profile</button>}
                {isAuthenticated && <button onClick={handleLogout}>Logout</button>}
                <button onClick={handleRegister}>Register</button>
                <button onClick={handleLogin}>Log In</button>
            </nav>
        </header>
    );
}

export default Header;