// components/SideBar.jsx
import React, { useState } from "react";
import './SideBar.css';

function SideBar({ searchQuery, setSearchQuery, applyFilters }) {
    // Filter state variables
    const [price, setPrice] = useState('');
    const [health, setHealth] = useState(false);
    const [glutenFree, setGlutenFree] = useState(false);
    const [nutAllergySafe, setNutAllergySafe] = useState(false);

    const handlePriceClick = (level) => {
        setPrice(level);
        applyFilters(level, health, glutenFree, nutAllergySafe);
    };

    const handleHealthChange = () => {
        const newHealth = !health;
        setHealth(newHealth);
        applyFilters(price, newHealth, glutenFree, nutAllergySafe);
    };

    const handleAllergyChange = (type) => {
        if (type === 'gluten') {
            const newState = !glutenFree;
            setGlutenFree(newState);
            applyFilters(price, health, newState, nutAllergySafe);
        } else if (type === 'nut') {
            const newState = !nutAllergySafe;
            setNutAllergySafe(newState);
            applyFilters(price, health, glutenFree, newState);
        }
    };

    const handleSearchInputChange = (e) => {
        setSearchQuery(e.target.value);
    };

    return (
        <div className="sideBar">
            <div className="sideBarContent">
                <h3>Healthy Foods</h3>
                <form>
                    <input
                        type="checkbox"
                        id="healthCheckBox"
                        checked={health}
                        onChange={handleHealthChange}
                    />
                    <label htmlFor="healthCheckBox">Healthy Choices</label>
                </form>
                <h3>Price Rating</h3>
                <form>
                    <button
                        type="button"
                        id="cheapButton"
                        className={price === '$$' ? 'active' : ''}
                        onClick={() => handlePriceClick('$$')}
                    >$$</button>
                    <button
                        type="button"
                        id="middleButton"
                        className={price === '$$$' ? 'active' : ''}
                        onClick={() => handlePriceClick('$$$')}
                    >$$$</button>
                    <button
                        type="button"
                        id="expensiveButton"
                        className={price === '$$$$' ? 'active' : ''}
                        onClick={() => handlePriceClick('$$$$')}
                    >$$$$</button>
                </form>
                <h3>Food Allergies</h3>
                <form>
                    <input
                        type="checkbox"
                        id="glutenAllergy"
                        checked={glutenFree}
                        onChange={() => handleAllergyChange('gluten')}
                    />
                    <label htmlFor="glutenAllergy">Gluten Free</label>
                    <br />
                    <input
                        type="checkbox"
                        id="nutAllergy"
                        checked={nutAllergySafe}
                        onChange={() => handleAllergyChange('nut')}
                    />
                    <label htmlFor="nutAllergy">Nut Allergy Safe</label>
                </form>
                <h3>Search Restaurants</h3>
                <input
                    type="text"
                    value={searchQuery}
                    onChange={handleSearchInputChange}
                    placeholder="Search by Name"
                />
            </div>
        </div>
    );
}

export default SideBar;
