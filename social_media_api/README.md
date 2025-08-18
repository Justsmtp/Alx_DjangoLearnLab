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

📌 Likes & Notifications Feature
Overview

This update enhances the Social Media API by adding likes and notifications functionality to improve user engagement.

Users can like/unlike posts.

Users receive notifications for important activities such as:

Someone liking their post

Gaining a new follower

Receiving comments

✅ Features Implemented
1. Like Model (in posts app)

Tracks which users liked which posts.

Ensures a user can only like a post once.

Fields:

user → ForeignKey to User

post → ForeignKey to Post

created_at → Timestamp of like

2. Notification Model (in notifications app)

Stores notifications for user interactions.

Fields:

recipient → User receiving the notification

actor → User performing the action (liking, following, commenting)

verb → Short description of action (e.g., "liked your post")

target → GenericForeignKey to the object (e.g., Post, Comment)

timestamp → When it happened

is_read → Boolean for read/unread status

🔗 API Endpoints
📍 Likes
Method	Endpoint	Description
POST	/posts/<int:pk>/like/	Like a post
POST	/posts/<int:pk>/unlike/	Unlike a post

Example request (authenticated user):

POST /posts/5/like/
Authorization: Bearer <token>


Example response:

{
  "status": "success",
  "message": "Post liked successfully."
}

📍 Notifications
Method	Endpoint	Description
GET	/notifications/	Retrieve all notifications for the logged-in user
GET	/notifications/?unread=true	Retrieve unread notifications only

Example response:

[
  {
    "id": 1,
    "actor": "john_doe",
    "verb": "liked your post",
    "timestamp": "2025-08-18T10:45:32Z",
    "is_read": false
  }
]

⚙️ How It Works

Liking a Post

Creates an entry in the Like model.

Generates a notification for the post’s owner.

Unliking a Post

Deletes the entry from the Like model.

No new notification is created.

Notifications System

Triggered when:

A post is liked.

A user is followed.

A comment is made.

Notifications are retrievable via /notifications/.

Users can filter unread notifications.

🧪 Testing

Liking/unliking posts was tested via Postman and Django tests.

Notifications were verified for:

Likes

Follows

Comments

Confirmed ordering by newest first.

## Setup
```bash
git clone https://github.com/Justsmtp/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/social_media_api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
