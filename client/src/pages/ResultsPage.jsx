// ResultsPage.jsx
import React, { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import Header from '../components/header';
import SideBar from '../components/sideBar';
import RestaurantList from '../components/RestaurantList';
import './ResultsPage.css';

function useQuery() {
  return new URLSearchParams(useLocation().search);
}
function ResultsPage() {
  const queryParams = useQuery();
  const initialSearchQuery = queryParams.get('q') || '';
  const [searchResults, setSearchResults] = useState([]);
  const [searchQuery, setSearchQuery] = useState(initialSearchQuery);
  const [filters, setFilters] = useState({ price: '', health: false, glutenFree: false, nutAllergySafe: false });

  useEffect(() => {
      const params = new URLSearchParams();
      if (searchQuery) params.set('q', searchQuery);
      if (filters.price) params.set('price', filters.price);
      if (filters.health) params.set('health', '1'); // Example health filter
      if (filters.glutenFree) params.set('allergy', 'gluten-free');
      if (filters.nutAllergySafe) params.set('allergy', 'nut-allergy-safe');

      fetch(`http://127.0.0.1:8000/api/search/?${params.toString()}`)
          .then((response) => response.json())
          .then((data) => setSearchResults(data))
          .catch((error) => console.error('Error fetching data:', error));
  }, [searchQuery, filters]);

  const applyFilters = (price, health, glutenFree, nutAllergySafe) => {
      setFilters({ price, health, glutenFree, nutAllergySafe });
  };

  return (
      <div>
          <Header />
          <SideBar searchQuery={searchQuery} setSearchQuery={setSearchQuery} applyFilters={applyFilters} />
          <div className="results-list-container">
              <RestaurantList restaurants={searchResults} />
          </div>
      </div>
  );
}

export default ResultsPage;
