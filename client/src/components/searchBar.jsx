// components/SearchBar.jsx
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './SearchBar.css';

function SearchBar() {
    const [query, setQuery] = useState('');
    const navigate = useNavigate();

    const search = (e) => {
        e.preventDefault();
        navigate('/results');
    };
    const handleSearch = (e) => {
        e.preventDefault();
        navigate(`/results?q=${encodeURIComponent(query)}`);
    };
    return (
        <div className="search-icon-container">
            <h1>Find Your Perfect Night Out!</h1>
            <form className="searchbar" onSubmit={handleSearch}>
                <input
                    type="text"
                    id="search"
                    placeholder="Search for restaurants, bars, and more!"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                />
                <button type="submit">Find Places!</button>
            </form>
        </div>
    );
}

export default SearchBar;
