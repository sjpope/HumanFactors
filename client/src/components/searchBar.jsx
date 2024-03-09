import React from 'react';

function SearchBar() {
    return (
        <div class="search-icon-container">
            <h1>Find Your Perfect Night Out!</h1>
                <form>
                    <input type="text" id="search" placeholder="Search"></input>
                    <button type="submit">Find Places!</button>
                </form>
        </div>
    );
}

export default SearchBar;