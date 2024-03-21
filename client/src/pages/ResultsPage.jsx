import React from 'react';
import '../App.css';
import Header from '../components/header';
import SideBar from '../components/sideBar';
import RestaurantList from '../components/restaurantResults';

function ResultsPage() {

    return (
        <div>
            <Header />
            <SideBar />
            <RestaurantList />
        </div>
    );
}

export default ResultsPage