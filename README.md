# Food Recipe Manager App

## Overview
The **Food Recipe Manager App** is a Django-based web application that allows users to create, update, and manage recipes. Users can provide details such as the dish name, description, recipe instructions, dish type, and an image of the dish.

##  Features
- Add new recipes with details
- Edit and update existing recipes
- Upload images for each recipe
- Display recipes in a structured format

##  Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS
- **Database:** SQLite (default, can be changed to PostgreSQL or MySQL)

##  Project Structure
```
food_recipe_manager/
│── recipe_app/      # Main Django app
│   ├── migrations/  # Database migrations
│   ├── static/      # Static files (CSS, JS, images)
│   ├── templates/   # HTML templates
│   ├── models.py    # Database models
│   ├── views.py     # Business logic
│   ├── urls.py      # URL routing
│   ├── forms.py     # Django forms
│   ├── admin.py     # Admin panel configuration
│── media/          # Uploaded images
│── food_recipe_manager/ # Project settings
│── db.sqlite3      # Database (SQLite by default)
│── manage.py       # Django management script
```

## Installation and Setup

###  Clone the repository
```bash
git clone https://github.com/yourusername/food-recipe-manager.git
cd food-recipe-manager
```

###  Create and activate a virtual environment
```bash
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

###  Install dependencies
```bash
pip install -r requirements.txt
```

###  Apply database migrations
```bash
python manage.py migrate
```

###  Create a superuser (for admin panel)
```bash
python manage.py createsuperuser
```
Follow the prompts to set up a username and password.

### Run the development server
```bash
python manage.py runserver
```
Visit **http://127.0.0.1:8000/** in your browser.

## Usage
1. Open the application in your browser.
2. Add new recipes using the form.
3. Update existing recipes via the edit button.
4. Upload images for each dish.

##  Troubleshooting
- If the form does not submit properly, ensure that `request.FILES` is handled in `views.py`:
  ```python
  form = DishForm(request.POST, request.FILES, instance=obj)
  ```
- Make sure your `media/` folder is correctly configured in `settings.py`:
  ```python
  MEDIA_URL = '/media/'
  MEDIA_ROOT = BASE_DIR / 'media'
  ```


