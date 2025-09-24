tablet-dashboard-navigation/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── database.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── navigation.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_navigation.py
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── alembic/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── NavigationMenu.tsx
│   │   ├── App.tsx
│   │   ├── index.tsx
│   ├── package.json
│   ├── tailwind.config.js
│   ├── tsconfig.json
├── README.md
├── docker-compose.yml

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

import React from 'react';
import NavigationMenu from './components/NavigationMenu';

const App = () => {
    return (
        <div className="App">
            <NavigationMenu />
        </div>
    );
};

export default App;

import React from "react";
import ReactDOM from "react-dom";
import './index.css';
import App from "./App";

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);

module.exports = {
  purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  darkMode: false,
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}

{
  "name": "tablet-dashboard-navigation",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-scripts": "4.0.3",
    "tailwindcss": "^2.1.2",
    "typescript": "^4.1.2"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}

version: '3.8'

services:
  backend:
    build:
      context: ./backend
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000
    volumes:
      - ./backend:/usr/src/app
    ports:
      - "8000:8000"
    depends_on:
      - db
  frontend:
    build:
      context: ./frontend
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/usr/src/app
    command: npm start
  db:
    image: postgres:12
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: db_name

volumes:
  postgres_data:

fastapi
sqlalchemy
psycopg2-binary
uvicorn

{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx"
  },
  "include": ["src"]
}

1. Navigate to the `backend` directory:

2. Create a `.env` file if necessary for environment-specific configurations.

3. Install dependencies:

4. Run the development server:

1. Navigate to the `frontend` directory:

2. Install dependencies:

3. Start the development server:

1. Run Docker Compose from the project root directory:

1. Navigate to the `backend` directory:

2. Run the tests:

## Contribution Guidelines

Please follow the standard practices for PR reviews and code contributions. Ensure unit tests are included and documentation is updated for any new functionalities.