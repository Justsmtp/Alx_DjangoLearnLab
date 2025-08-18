# Social Media API - Project Setup & User Authentication

This is the first milestone of the **Social Media API**, focusing on project setup, custom user model, and authentication system.

## Features
- Django + Django REST Framework setup
- Custom user model with:
  - Bio
  - Profile picture
  - Followers/Following relationship
- Token authentication
- Endpoints:
  - `/api/accounts/register/`
  - `/api/accounts/login/`
  - `/api/accounts/profile/`

## Setup
```bash
git clone https://github.com/Justsmtp/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/social_media_api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
