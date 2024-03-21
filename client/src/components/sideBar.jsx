import React from "react";

function SideBar() {
    return (
        <div className = "sideBar">
            <div className="sideBarContent">
                <h3>Healthy Foods</h3>
                <form>
                    <input type="checkbox" id="healthCheckBox"></input>
                    <label for="healthCheckBox">Healthy Choices</label><br/>
                </form>
                <h3>Price Rating</h3>
                <form>
                    <button id="cheapButton">$$</button>
                    <button id="middleButton">$$$</button>
                    <button id="expensiveButton">$$$$</button>
                </form>
                <h3>Food Allergies</h3>
                <form>
                    <input type="checkbox" id="glutenAllergy"></input>
                    <label for="glutenAllergy">Gluten Free</label><br/>
                    <input type="checkbox" id="nutAllergy"></input>
                    <label for="nutAllergy">Nut Allergy Safe</label><br/>
                </form>
            </div>
        </div>
    )
}

export default SideBar;