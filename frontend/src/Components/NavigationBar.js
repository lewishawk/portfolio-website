import "./css/NavigationBar.css"
import React from "react"
import { Link } from 'react-router-dom';

const NavigationBar = () => {
    return (
        <div className = "NavigationBar">
            <Link to="/">Home</Link>
            <Link to="/blog">Blog</Link>
        </div>
    );
}

export default NavigationBar;