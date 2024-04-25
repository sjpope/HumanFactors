import React from 'react';
import { useNavigate } from 'react-router-dom';

function Header() {
    const navigate = useNavigate();

    const handleRegister = (e) => {
        e.preventDefault();
        
        // Here you would typically open a registration modal or navigate to a registration page
        navigate('/api/register');

        // Since it's a form submission, you'd handle the registration via an API call.
    };

    const handleLogin = (e) => {
        e.preventDefault();
        navigate('/api/login'); // Assuming you have a route set up for login
    };

    return (
        <header>
            <h1>EasyBook</h1>
            <nav>
                <button onClick={handleRegister}>Register</button>
                <button onClick={handleLogin}>Log In</button>
            </nav>
        </header>
    );
}

export default Header;