# Membership Directory

A web application for managing company memberships. Users can register, login, and manage their company details. The application includes search functionality to find companies by name, description, or industry.

## Features

- User Authentication (Register/Login)
- Company Profile Management
- Company Directory Listing
- Search Functionality
- Responsive Design using Bootstrap

## Installation

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python run.py
```

The application will be available at `http://localhost:5000`

## Usage

1. Register a new account
2. Login with your credentials
3. Add your company details
4. Browse other companies
5. Use the search function to find specific companies

## Technologies Used

- Python Flask
- SQLAlchemy
- Flask-Login for authentication
- Bootstrap for UI
- SQLite database
