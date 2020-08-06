# BBCF Website

## 1. Set up the repository

- Clone the repository from Github
- Make sure you have Python 3.7, pip3, pipenv and PostgreSQL installed on your machine
- Navigate to the repository and run `pipenv install`
- Create a postgres database called `bbcf`
- Apply migrations by running the command `flask db upgrade`
- To start the website, run the app.py file with `python app.py` or `./app.py`

## Admin interface

- The admin interface is password protected, you need to have a user and password already set up
- To log into the admin interface, go to the /admin url
