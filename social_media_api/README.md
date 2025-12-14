# Social Media API

## Features
- User registration & authentication
- Follow / Unfollow users
- User feed displaying posts from followed users

## Endpoints
### Accounts
- `POST /accounts/follow/<user_id>/` : Follow a user
- `POST /accounts/unfollow/<user_id>/` : Unfollow a user

### Posts
- `GET /posts/feed/` : Get posts from users you follow

## Setup
```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
