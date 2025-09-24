import React from "react";
import { useState, useEffect } from "react";

const NavigationMenu = () => {
    const [navItems, setNavItems] = useState([]);

    useEffect(() => {
        fetch('/api/v1/navigation/')
            .then(response => response.json())
            .then(data => setNavItems(data));
    }, []);

    return (
        <nav>
            <ul>
                {navItems.map(item => (
                    <li key={item.id}>
                        <a href={item.link}>
                            <img src={item.icon} alt={`${item.name} icon`} />
                            {item.name}
                        </a>
                    </li>
                ))}
            </ul>
        </nav>
    );
};

export default NavigationMenu;