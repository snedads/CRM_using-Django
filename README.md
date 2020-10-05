# CRM

![GitHub](https://img.shields.io/github/license/snedads/CRM_using-Django)

CRM (Customer relationship management) is a simple project built using Python and Django.

## Software Used
* [Visual Studio Code](https://code.visualstudio.com/download)

## Running the application

- To run the Django app on your local computer, set up a Python development environment, including Python, `pip`, and `virtualenv`.
- Create an isolated Python environment, and install dependencies:
  ```
  virtualenv env
  ```
  > To activate your virtual environment use this command(windows):
  ```
  env\scripts\activate
  ```
  > To install all the requirements for the project:
  ```
  pip install -r requirements.txt
  ```
- Run the Django migrations to set up your models:
  ```
  python manage.py makemigrations
  python manage.py migrate
  ```
- Start a local web server:
  ```
  python manage.py runserver
  ```
- In your browser, go to [http://localhost:8000](http://localhost:8000).
- Press `Control+C` to stop the local web server.

## Using the Django admin console

- Create a superuser. You need to define a username and password.
  ```
  python manage.py createsuperuser
  ```
- Start a local web server:
  ```
  python manage.py runserver
  ```
- In your browser, go to [http://localhost:8000/admin](http://localhost:8000/admin).
- Log in to the admin site using the username and password you used when you ran `createsuperuser`.
