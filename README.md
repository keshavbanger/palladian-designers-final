# Palladian Designers Project

This repository contains the full source code and assets for the Palladian Designers platform. It has been organized for maximum clarity and maintainability.

## 📂 Project Structure

### 🏗️ Backend (Django)
- **`palladian/`**: The core project configuration, containing `settings.py`, `urls.py`, and `wsgi.py`.
- **`core/`**: The primary application handling project portfolios, testimonials, and the main website logic.
- **`careers/`**: An independent module for job listings and candidate applications.
- **`manage.py`**: The standard Django command-line utility.

### 🎨 Frontend
- **`templates/`**: All HTML templates for the website, organized by app.
- **`static/`**: Global frontend assets including:
  - `css/`: Theme-wide styling.
  - `js/`: Interactive elements and animations.
  - `img/`: Logos and static design assets.
  - `font/`: Custom typography.

### 🖼️ Media & Data
- **`media/`**: All dynamic content uploaded through the admin panel, such as project photos and client logos.
- **`db.sqlite3`**: The local database file containing all project and content records.

### 🚀 Deployment
- **`vercel.json`**: Configuration for serverless deployment on Vercel.
- **`requirements.txt`**: List of Python dependencies.
- **`.env`**: Environment variables (secrets) for the app.

## 🛠️ Getting Started
1. Install dependencies: `pip install -r requirements.txt`
2. Apply migrations: `python manage.py migrate`
3. Start the server: `python manage.py runserver`
