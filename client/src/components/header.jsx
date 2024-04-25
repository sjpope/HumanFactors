// header.jsx
import React from 'react';
import { useNavigate } from 'react-router-dom';

function Header() {
    const navigate = useNavigate();

    const handleRegister = (e) => {
        e.preventDefault();
        navigate('/register'); // Updated to use the client-side path for register
    };

    const handleLogin = (e) => {
        e.preventDefault();
        navigate('/login'); // Updated to use the client-side path for login
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