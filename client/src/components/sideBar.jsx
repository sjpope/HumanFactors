import React from "react";

function SideBar() {
    return (
        <div className = "sideBar">
            <h3>Health Rating</h3>
            <div className="sideBarContent">
                <form>
                    <input type="checkbox" id="healthCheckBox"></input>
                    <label for="healthCheckBox">Very Healthy Choices</label><br/>
                    <input type="checkbox" id="unhealthyCheckBox"></input>
                    <label for="healthCheckBox">Not The Best</label><br/>
                </form>
            </div>
        </div>
    )
}

export default SideBar;