# HotBeansWeb – Basic Python Flask Project

This project demonstrates a user sign-up and login approach for HotBeansWeb using Python Flask for the backend and plain HTML/CSS/JavaScript for the frontend.

## Features

- Simple JSON-based user storage
- Sign Up functionality
- Login/Logout from any page
- Remember Me functionality
- Dynamic navigation based on authentication status

## Setup Instructions

1. Make sure you have Python 3.6+ installed
2. Run the setup script to install dependencies:

```
python setup.py
```

3. Use a local development server like VSCode Live Server to serve the front-end
   - If using VSCode, install the Live Server extension
   - Right-click on any HTML file and select "Open with Live Server"
   - The front-end will be available at http://127.0.0.1:5500

4. Start the Python Flask server in a separate terminal:

```
python server.py
```

5. Access the application:
   - http://127.0.0.1:5500/index.html - Home page
   - http://127.0.0.1:5500/signin.html - Sign Up page
   - http://127.0.0.1:5500/login.html - Login page

## API Endpoints

- POST `/api/signup` - Register a new user
- POST `/api/login` - Authenticate a user

## Technical Details

- Backend: Flask (Python)
- Data Storage: JSON file (users.json)
- No password hashing (simple test implementation)
- Session management via browser's sessionStorage or localStorage

## Note

This is a simplified implementation for **learning purposes only**. In a production environment, you would want to:

- Use a proper database instead of JSON files
- Implement password hashing (e.g., bcrypt)
- Use secure cookies for session management
- Add CSRF protection
- Use HTTPS
- Implement proper input validation and sanitization