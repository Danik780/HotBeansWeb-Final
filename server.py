from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os
import uuid
from datetime import datetime

app = Flask(__name__)

# Enable CORS specifically for the Live Server origin
CORS(app, resources={r"/api/*": {"origins": ["http://127.0.0.1:5500", "http://localhost:5500"]}})

# Directory for data storage (not served to the public)
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
os.makedirs(DATA_DIR, exist_ok=True)

# File path for user data (now in 'data/users.json')
USERS_FILE = os.path.join(DATA_DIR, 'users.json')

# Initialize users file if it doesn't exist
if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, 'w') as f:
        json.dump([], f)

# Helper functions for user management
def get_users():
    try:
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    except:
        return []

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

# Serve static files from the "static" folder
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

# API Routes
@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.json
    
    # Extract form data
    firstname = data.get('firstname', '')
    lastname = data.get('lastname', '')
    email = data.get('email', '')
    password = data.get('password', '')  # Plain text as requested
    
    # Basic validation
    if not firstname or not lastname or not email or not password:
        return jsonify({'success': False, 'message': 'All fields are required'}), 400
    
    # Get existing users
    users = get_users()
    
    # Check for existing email
    if any(user['email'] == email for user in users):
        return jsonify({'success': False, 'message': 'Email already registered'}), 400
    
    # Create new user
    new_user = {
        'id': str(uuid.uuid4()),
        'firstname': firstname,
        'lastname': lastname,
        'email': email,
        'password': password,  # Storing as plain text
        'created': datetime.now().isoformat()
    }
    
    # Add to users and save
    users.append(new_user)
    save_users(users)
    
    # Return user info (excluding password)
    user_info = new_user.copy()
    user_info.pop('password')
    
    return jsonify({
        'success': True,
        'message': 'Account created successfully',
        'user': user_info
    }), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    
    # Extract form data
    email = data.get('email', '')
    password = data.get('password', '')
    
    # Basic validation
    if not email or not password:
        return jsonify({'success': False, 'message': 'Email and password are required'}), 400
    
    # Get users
    users = get_users()
    
    # Find user by email
    user = None
    for u in users:
        if u['email'] == email:
            user = u
            break
    
    # Check if user exists and password matches
    if not user or user['password'] != password:
        return jsonify({'success': False, 'message': 'Invalid email or password'}), 401
    
    # Return user info (excluding password)
    user_info = user.copy()
    user_info.pop('password')
    
    return jsonify({
        'success': True,
        'message': 'Login successful',
        'user': user_info
    })

@app.route('/api/user/<user_id>', methods=['GET'])
def get_user(user_id):
    users = get_users()
    
    # Find user by ID
    user = next((u for u in users if u['id'] == user_id), None)
    
    if not user:
        return jsonify({'success': False, 'message': 'User not found'}), 404
    
    # Return user info (excluding password)
    user_info = user.copy()
    user_info.pop('password')
    
    return jsonify({
        'success': True,
        'user': user_info
    })

@app.route('/api/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    users = get_users()
    
    # Extract form data
    firstname = data.get('firstname', '')
    lastname = data.get('lastname', '')
    email = data.get('email', '')
    
    # Basic validation
    if not firstname or not lastname or not email:
        return jsonify({'success': False, 'message': 'All fields are required'}), 400
    
    # Find user index
    user_index = None
    for i, u in enumerate(users):
        if u['id'] == user_id:
            user_index = i
            break
    
    if user_index is None:
        return jsonify({'success': False, 'message': 'User not found'}), 404
    
    # Check for duplicate email
    if any(u['email'] == email and u['id'] != user_id for u in users):
        return jsonify({'success': False, 'message': 'Email already registered to another account'}), 400
    
    # Update user
    users[user_index]['firstname'] = firstname
    users[user_index]['lastname'] = lastname
    users[user_index]['email'] = email
    
    # Save changes
    save_users(users)
    
    # Return updated user info (excluding password)
    user_info = users[user_index].copy()
    user_info.pop('password')
    
    return jsonify({
        'success': True,
        'message': 'Profile updated successfully',
        'user': user_info
    })

if __name__ == '__main__':
    print("Server running at http://127.0.0.1:5000")
    print("Users file path:", os.path.abspath(USERS_FILE))
    print("CORS enabled for: http://127.0.0.1:5500, http://localhost:5500")
    print("To test the authentication system:")
    print("1. Serve the front-end from the 'static' folder using VSCode Live Server (http://127.0.0.1:5500)")
    print("2. Run this Python server in a terminal (http://127.0.0.1:5000)")
    print("3. Go to http://127.0.0.1:5500/signin.html to create an account")
    print("4. Go to http://127.0.0.1:5500/login.html to log in")
    app.run(host='127.0.0.1', port=5000, debug=True)
