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

🔹 Post Endpoints
List Posts

Request

GET /api/posts/


Response (200 OK)

{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "author": 1,
      "author_username": "john_doe",
      "title": "My First Post",
      "content": "Hello, this is my first post!",
      "created_at": "2025-08-18T10:30:00Z",
      "updated_at": "2025-08-18T10:30:00Z",
      "comments": []
    },
    {
      "id": 2,
      "author": 2,
      "author_username": "jane_smith",
      "title": "Another Post",
      "content": "This is another example post.",
      "created_at": "2025-08-18T11:00:00Z",
      "updated_at": "2025-08-18T11:00:00Z",
      "comments": []
    }
  ]
}

Create a Post

Request

POST /api/posts/
Authorization: Token <user_token>
Content-Type: application/json

{
  "title": "My First Post",
  "content": "Hello, this is my first post!"
}


Response (201 Created)

{
  "id": 1,
  "author": 1,
  "author_username": "john_doe",
  "title": "My First Post",
  "content": "Hello, this is my first post!",
  "created_at": "2025-08-18T10:30:00Z",
  "updated_at": "2025-08-18T10:30:00Z",
  "comments": []
}

Retrieve a Post (with Comments)

Request

GET /api/posts/1/


Response

{
  "id": 1,
  "author": 1,
  "author_username": "john_doe",
  "title": "My First Post",
  "content": "Hello, this is my first post!",
  "created_at": "2025-08-18T10:30:00Z",
  "updated_at": "2025-08-18T10:30:00Z",
  "comments": [
    {
      "id": 1,
      "post": 1,
      "author": 2,
      "author_username": "jane_smith",
      "content": "Nice post!",
      "created_at": "2025-08-18T10:45:00Z",
      "updated_at": "2025-08-18T10:45:00Z"
    }
  ]
}

🔹 Comment Endpoints
Create a Comment

Request

POST /api/comments/
Authorization: Token <user_token>
Content-Type: application/json

{
  "post": 1,
  "content": "Nice post!"
}


Response (201 Created)

{
  "id": 1,
  "post": 1,
  "author": 2,
  "author_username": "jane_smith",
  "content": "Nice post!",
  "created_at": "2025-08-18T10:45:00Z",
  "updated_at": "2025-08-18T10:45:00Z"
}

Update or Delete a Comment (Author Only)

Update Request

PUT /api/comments/1/
Authorization: Token <user_token>
Content-Type: application/json

{
  "post": 1,
  "content": "Updated comment text"
}


Delete Request

DELETE /api/comments/1/
Authorization: Token <user_token>

🔹 Features Implemented

✅ CRUD for posts and comments

✅ Authors can only edit/delete their own content

✅ Pagination for listing endpoints (PAGE_SIZE=10)

✅ Search posts by title or content


🔹 Follow & Feed API
Follow a User
POST /api/accounts/follow/<user_id>/

Unfollow a User
POST /api/accounts/unfollow/<user_id>/

List Who You’re Following
GET /api/accounts/following/

Get Personalized Feed
GET /api/posts/feed/

## Setup
```bash
git clone https://github.com/Justsmtp/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/social_media_api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
