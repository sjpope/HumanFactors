import React, { useState } from 'react';

function Register() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    // TODO: Implement the register functionality
    const handleSubmit = (event) => {
        event.preventDefault();
        fetch('http://127.0.0.1:8000/api/register/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.token) {
                localStorage.setItem('token', data.token);
                window.location.href = "/";  // Redirect to home on success
            } else {
                setError('Failed to Register');
            }
        })
        .catch(() => setError('Failed to Register'));
    };
    // form validation & improvements here
    return (
        <div className="form-container">
            <form onSubmit={handleSubmit} className="register-form">
                <label>
                    Username:
                    <input type="text" value={username} onChange={e => setUsername(e.target.value)} />
                </label>
                <label>
                    Password:
                    <input type="password" value={password} onChange={e => setPassword(e.target.value)} />
                </label>
                <button type="submit">Register</button>
                {error && <p>{error}</p>}
            </form>
        </div>
    );
}

export default Register;
