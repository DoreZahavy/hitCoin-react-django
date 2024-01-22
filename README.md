# hitCoin: Money Management and Bitcoin Market Analysis
## Overview
Hitcoin is a comprehensive money management system designed to streamline financial transactions, track expenses, and provide insightful statistics about the Bitcoin market. The project combines the power of PostgreSQL for efficient data organization, Django Rest Framework for API endpoints, React for a dynamic user interface, Chart.js for data visualization, and Redux for state management.

## Features

**PostgreSQL Database:**
* Utilizes a relational database with one-to-many and many-to-many relationships for efficient querying and data organization.
* Tables for moves (money transfers) connected to users through foreign keys.
* Users and contacts are interconnected, allowing seamless navigation and association between users.

**Django Rest Framework:**
* Implements DRF to manage data models and organize CRUD endpoints.
* Utilizes generic classes and decorators to simplify view logic.

**React:**
* Built with React, leveraging reusable components for a modular and maintainable codebase.
* Implements hooks and custom hooks, enhancing the efficiency of useEffect and form handling.
* Uses React Router for seamless navigation between different pages.

**Chart.js:**
* Custom functions to tailor data sent to Chart.js components, enabling clean and visually appealing data charts.
* Integration with blockchain.info API to dynamically fetch Bitcoin market data.
* Implements a caching mechanism to limit API calls, ensuring optimal performance.

**Redux:**
* Utilizes classic Redux for unopinionated control over application state.
* Implements initial state, actions, and reducers for organized state management.

**Security**
* Incorporates a route guard to redirect users to the login page if not authenticated, ensuring secure access to sensitive information.
* Attaches an encrypted session token in the cookie upon login to identify logged-in users securely.
* Implements one-sided encryption for passwords before saving them to the database, providing an additional layer of security. This ensures that even developers do not have access to plain-text passwords.
* Guards against CSRF attacks by attaching a token to the cookie and sending it in the request headers from the frontend. This helps verify the authenticity of requests and prevents unauthorized actions.
