# Chefster Backend App

## Prerequisites

- Python >= v3.10
- Postgresql >= 14.0

## Local Dev Setup

- Close this repo `git clone <repo_url> <folder_on_your_machine>`
- Create Virtual Env `python3 -m venv env`
- Activate Virtual Env `source ./env/bin/activate`
- Install dependencies `pip install -r requirements.txt`
- Run the Migrations `python manage.py migrate`
- Run the App `python manage.py runserver`