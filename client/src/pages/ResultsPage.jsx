import React, { useState, useEffect } from 'react';
import Header from '../components/header';
import SideBar from '../components/sideBar';
import RestaurantList from '../components/RestaurantList';
import './ResultsPage.css';

function ResultsPage() {
    const [searchResults, setSearchResults] = useState([]);
    const [searchQuery, setSearchQuery] = useState('');

    useEffect(() => {
        if (searchQuery !== '') {
            fetch(`http://127.0.0.1:8000/api/search/?q=${encodeURIComponent(searchQuery)}`)
                .then(response => response.json())
                .then(data => setSearchResults(data))
                .catch(error => console.error('Error fetching data:', error));
        }
    }, [searchQuery]);

    return (
        <div>
            <Header />
            <SideBar searchQuery={searchQuery} setSearchQuery={setSearchQuery} />
            <div className="results-list-container">
                <RestaurantList restaurants={searchResults} />
            </div>
        </div>
    );
}

export default ResultsPage;
