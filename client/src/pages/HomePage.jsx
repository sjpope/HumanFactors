import React, { useState, useEffect } from 'react';
import Header from '../components/header';
import SearchBar from '../components/searchBar';
import RestaurantCard from '../components/restaurantCard';
import Footer from '../components/footer';
import { Link } from 'react-router-dom';
import './HomePage.css';

function HomePage() {
    const isAuthenticated = localStorage.getItem('token');
    const [restaurants, setRestaurants] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/restaurants/')
            .then(response => response.json())
            .then(data => setRestaurants(data))
            .catch(error => console.error('Error fetching data: ', error));
    }, []);

    return (
        <div>
            <Header />
            <SearchBar />
            {/* <div className="profile-container">
                {isAuthenticated && <Link to="/profile">My Profile</Link>}
            </div> */}
            <div className="restaurant-cards-container">
                {restaurants.map((restaurant, index) => (
                    <Link to={`/restaurant/${restaurant.id}`} key={index} className="restaurant-card-link">
                        <RestaurantCard name={restaurant.name} cuisine={restaurant.cuisine_type} />
                    </Link>
                ))}
            </div>
            <Footer />
        </div>
    );
}

export default HomePage;