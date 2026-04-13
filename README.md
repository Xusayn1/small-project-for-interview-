# Small Project for Interview (Django Backend)

This is a backend project built with **Django** for interview practice purposes.  
The main focus of this project is implementing a **custom authentication system without using Django built-in authentication system (`django.contrib.auth`)**.

---

## 🚀 Features

- Custom User Model (built from scratch)
- Custom Authentication system (Login / Register)
- Password hashing and validation
- Token/session-based authentication (if used in your project)
- CRUD-ready backend structure
- REST API endpoints (if applicable)

---

## 🛠 Tech Stack

- Python 3.x
- Django
- Django REST Framework (if used)
- SQLite (default database)

---

## 🔐 Authentication System

Instead of using Django’s built-in authentication system, this project implements:

- Custom user model
- Manual password hashing (e.g. `make_password`, `check_password`)
- Custom login logic
- Session or token handling (depending on implementation)

This approach was made to better understand how authentication works internally.

---

## 📂 Project Structure
project /
| 
| --- access
| --- accounts
| --- common 
| --- core 
|
| .gitignore
| Pipfile
| Pipfile.lock
| manage.py  


---

## ⚙️ Installation & Setup

```bash
# Clone repository
git clone https://github.com/Xusayn1/small-project-for-interview-.git

# Move into project
cd small-project-for-interview-

# Create virtual environment
python -m venv venv

# Activate venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver

📌 API Endpoints (Example)
POST /register/   - Create new user
POST /login/      - Login user
GET  /profile/    - Get user info (protected)

🎯 Purpose of This Project

This project was created to:

Understand how authentication works internally in Django
Practice backend development for interviews
Build clean and structured API logic without relying on built-in shortcuts

👨‍💻 Author

GitHub: @Xusayn1

📌 Note
This is a learning / interview preparation project, not a production-ready system.
