# Candidate management portal

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)

A portal to manage candidates, create candidates and search candidates with it's name

## Features
- ✅ User authentication 
- 📝 Content submission
- 📊 Admin dashboard for moderation
- 📊 Swagger doc to test the API's

## Tech Stack
- **Backend**: Django + Django REST Framework

## Installation
### 1. Clone the repository
```bash
git clone git@github.com:Sagarkkr/candidate_portal.git
```
### 2. Create virtual environment
```
python -m venv {env_name}
```
### 3. Move to project folder
```
cd candidate_portal/
```
### 4. Run migrations
```
python manage.py migrate
```
### 5. Create superuser
```
python manage.py createsuperuser
```
### 6. Final step run the server
```
python manage.py runserver
```
### 7. Token generation
```
Pass the user admin credentials used while creating super user to get the access token 
```