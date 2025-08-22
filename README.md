Auth System of Django for Login through Social Account

# Django Social Login Page

This project implements a **login system using Django** with **Google and Facebook authentication** via `django-allauth`. It provides a secure and scalable solution for user authentication.

----------

## Features

-   Social authentication with Google and Facebook
    
-   Simple and clean login template
    
-   Configurable authentication backends
    
-   Easy integration with custom user models
    
-   Ready for Bootstrap or Tailwind styling
    

----------

## Project Setup

1.  Install Python and Django.
    
2.  Create and activate a virtual environment.
    
3.  Start a Django project and add an authentication app.
    
4.  Install and configure `django-allauth` in `settings.py`.
    
5.  Add Google and Facebook provider credentials in Django Admin.
    
6.  Configure URLs to include `allauth` routes.
    
7.  Create a login template with provider login links.
    

----------

## How It Works

-   Users can log in via Google or Facebook.
    
-   Authentication is handled by `django-allauth`.
    
-   After login, users are redirected to the homepage.
    
-   Logout redirects users back to the homepage.
    

----------

## Enhancements

-   Add a custom user model for extra profile fields.
    
-   Style the login page using Bootstrap or Tailwind CSS.
    
-   Enable features like "Remember Me" and Two-Factor Authentication.
    
-   Deploy on production servers (Heroku, AWS, etc.).
    

----------

## Running the Project

-   Run migrations to set up the database.
    
-   Start the Django development server.
    
-   Test the login page at `/accounts/login/`.
    

----------

## Project Structure

`login_project/
│
├── login_project/ # Main project folder │   ├── __init__.py
│   ├── settings.py # Django settings (configured with allauth) │   ├── urls.py # Project URL configuration │   ├── asgi.py
│   └── wsgi.py
│
├── accounts/ # Sub app for authentication │   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── templates/ # Templates folder at project root │   └── account/
│       └── login.html # Social login template │
├── manage.py # Django management script └── db.sqlite3 # SQLite database (default)`
