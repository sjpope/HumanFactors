import React, { useState } from 'react';

function Register() {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password1, setPassword1] = useState('');
    const [password2, setPassword2] = useState('');
    const [error, setError] = useState('');

    // TODO: Implement the register functionality
    const handleSubmit = (event) => {
        event.preventDefault();
        if (password1 !== password2) {
            setError('Passwords do not match.');
            return;
        }
        fetch('http://127.0.0.1:8000/api/register/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, email, password1, password2 }),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.token) {
                localStorage.setItem('token', data.token);
                window.location.href = "/";  // Redirect to home on success
            } else {
                setError('Failed to Register');
            }
        })
        .catch((error) => {
            console.error('There has been a problem with your fetch operation:', error);
            setError('Failed to Register');
        });
    };

    // form validation & improvements here

    /*
    Django Register Form:

    class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)  

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.exists():
            raise ValidationError("Email already exists")
        return email

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit: 
            user.save()
        return user
    */

        return (
            <div className="form-container">
                <form onSubmit={handleSubmit} className="register-form">
                    <label>
                        Username:
                        <input type="text" value={username} onChange={e => setUsername(e.target.value)} />
                    </label>
                    <label>
                        Email:
                        <input type="email" value={email} onChange={e => setEmail(e.target.value)} />
                    </label>
                    <label>
                        Password:
                        <input type="password" value={password1} onChange={e => setPassword1(e.target.value)} />
                    </label>
                    <label>
                        Confirm Password:
                        <input type="password" value={password2} onChange={e => setPassword2(e.target.value)} />
                    </label>
                    <button type="submit">Register</button>
                    {error && <p>{error}</p>}
                </form>
            </div>
        );
}

export default Register;
