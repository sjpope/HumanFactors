import React from 'react';
import { useNavigate } from 'react-router-dom';

function SearchBar() {

    const navigate = useNavigate();

    const search = e => {
        e.preventDefault();
        navigate("/results");
    };

    return (
        <div class="search-icon-container">
            <h1>Find Your Perfect Night Out!</h1>
                <form className='searchbar' onSubmit={search}>
                    <input type="text" id="search" placeholder="Enter Location"></input>
                    <button type="submit">Find Places!</button>
                </form>
        </div>
    );
}

export default SearchBar;