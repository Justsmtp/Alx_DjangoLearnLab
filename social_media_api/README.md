# Social Media API - Project Setup & User Authentication

This is the first milestone of the **Social Media API**, focusing on project setup, custom user model, and authentication system.

## Live API Base URL
🌐 **Base URL**: `https://justsmtp.pythonanywhere.com`

## Features
- Django + Django REST Framework setup
- Custom user model with:
  - Bio
  - Profile picture
  - Followers/Following relationship
- Token authentication
- CRUD operations for posts and comments
- Like/Unlike functionality
- Notifications system
- User following/followers
- Personalized feed

## 📋 Complete API Endpoints Reference

### 🔐 Authentication Endpoints
| Method | Endpoint | Description | Test URL |
|--------|----------|-------------|----------|
| POST | `/api/accounts/register/` | Register new user | `https://justsmtp.pythonanywhere.com/api/accounts/register/` |
| POST | `/api/accounts/login/` | User login | `https://justsmtp.pythonanywhere.com/api/accounts/login/` |
| GET | `/api/accounts/profile/` | Get user profile | `https://justsmtp.pythonanywhere.com/api/accounts/profile/` |

### 👥 User Follow Endpoints
| Method | Endpoint | Description | Test URL |
|--------|----------|-------------|----------|
| POST | `/api/accounts/follow/<user_id>/` | Follow a user | `https://justsmtp.pythonanywhere.com/api/accounts/follow/1/` |
| POST | `/api/accounts/unfollow/<user_id>/` | Unfollow a user | `https://justsmtp.pythonanywhere.com/api/accounts/unfollow/1/` |
| GET | `/api/accounts/following/` | List who you're following | `https://justsmtp.pythonanywhere.com/api/accounts/following/` |

### 📝 Post Endpoints
| Method | Endpoint | Description | Test URL |
|--------|----------|-------------|----------|
| GET | `/api/posts/` | List all posts | `https://justsmtp.pythonanywhere.com/api/posts/` |
| POST | `/api/posts/` | Create a new post | `https://justsmtp.pythonanywhere.com/api/posts/` |
| GET | `/api/posts/<id>/` | Retrieve specific post | `https://justsmtp.pythonanywhere.com/api/posts/1/` |
| PUT | `/api/posts/<id>/` | Update post (author only) | `https://justsmtp.pythonanywhere.com/api/posts/1/` |
| DELETE | `/api/posts/<id>/` | Delete post (author only) | `https://justsmtp.pythonanywhere.com/api/posts/1/` |
| GET | `/api/posts/feed/` | Get personalized feed | `https://justsmtp.pythonanywhere.com/api/posts/feed/` |

### 💬 Comment Endpoints
| Method | Endpoint | Description | Test URL |
|--------|----------|-------------|----------|
| POST | `/api/comments/` | Create a comment | `https://justsmtp.pythonanywhere.com/api/comments/` |
| PUT | `/api/comments/<id>/` | Update comment (author only) | `https://justsmtp.pythonanywhere.com/api/comments/1/` |
| DELETE | `/api/comments/<id>/` | Delete comment (author only) | `https://justsmtp.pythonanywhere.com/api/comments/1/` |

### ❤️ Like Endpoints
| Method | Endpoint | Description | Test URL |
|--------|----------|-------------|----------|
| POST | `/api/posts/<id>/like/` | Like a post | `https://justsmtp.pythonanywhere.com/api/posts/1/like/` |
| POST | `/api/posts/<id>/unlike/` | Unlike a post | `https://justsmtp.pythonanywhere.com/api/posts/1/unlike/` |

### 🔔 Notification Endpoints
| Method | Endpoint | Description | Test URL |
|--------|----------|-------------|----------|
| GET | `/api/notifications/` | Get all notifications | `https://justsmtp.pythonanywhere.com/api/notifications/` |
| GET | `/api/notifications/?unread=true` | Get unread notifications | `https://justsmtp.pythonanywhere.com/api/notifications/?unread=true` |

## 🧪 Quick Testing Guide

### 1. Register a User
```bash
curl -X POST https://justsmtp.pythonanywhere.com/api/accounts/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "testpass123"
  }'
```

### 2. Login
```bash
curl -X POST https://justsmtp.pythonanywhere.com/api/accounts/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "testpass123"
  }'
```

### 3. Create a Post (with token)
```bash
curl -X POST https://justsmtp.pythonanywhere.com/api/posts/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token <your_token>" \
  -d '{
    "title": "Test Post",
    "content": "This is a test post"
  }'
```

### 4. List All Posts
```bash
curl -X GET https://justsmtp.pythonanywhere.com/api/posts/
```

## 📖 Detailed Endpoint Examples

### 🔹 Post Endpoints

#### List Posts
**Request**
```
GET https://justsmtp.pythonanywhere.com/api/posts/
```

**Response (200 OK)**
```json
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
    }
  ]
}
```

#### Create a Post
**Request**
```
POST https://justsmtp.pythonanywhere.com/api/posts/
Authorization: Token <user_token>
Content-Type: application/json

{
  "title": "My First Post",
  "content": "Hello, this is my first post!"
}
```

**Response (201 Created)**
```json
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
```

### 🔹 Comment Endpoints

#### Create a Comment
**Request**
```
POST https://justsmtp.pythonanywhere.com/api/comments/
Authorization: Token <user_token>
Content-Type: application/json

{
  "post": 1,
  "content": "Nice post!"
}
```

**Response (201 Created)**
```json
{
  "id": 1,
  "post": 1,
  "author": 2,
  "author_username": "jane_smith",
  "content": "Nice post!",
  "created_at": "2025-08-18T10:45:00Z",
  "updated_at": "2025-08-18T10:45:00Z"
}
```

### 🔹 Like Endpoints

#### Like a Post
**Request**
```
POST https://justsmtp.pythonanywhere.com/api/posts/1/like/
Authorization: Token <user_token>
```

**Response**
```json
{
  "status": "success",
  "message": "Post liked successfully."
}
```

### 🔹 Notification Endpoints

#### Get Notifications
**Request**
```
GET https://justsmtp.pythonanywhere.com/api/notifications/
Authorization: Token <user_token>
```

**Response**
```json
[
  {
    "id": 1,
    "actor": "john_doe",
    "verb": "liked your post",
    "timestamp": "2025-08-18T10:45:32Z",
    "is_read": false
  }
]
```

## ✅ Features Implemented

✅ CRUD for posts and comments  
✅ Authors can only edit/delete their own content  
✅ Pagination for listing endpoints (PAGE_SIZE=10)  
✅ Search posts by title or content  
✅ Like/Unlike functionality  
✅ User follow/unfollow system  
✅ Personalized feed based on followed users  
✅ Real-time notifications for user interactions  
✅ Token-based authentication  

## 🔧 Local Setup (Optional)
```bash
git clone https://github.com/Justsmtp/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/social_media_api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 📱 Testing Tools
- **Postman**: Import the endpoint URLs for easy testing
- **cURL**: Use the provided cURL examples
- **Browser**: Visit GET endpoints directly in your browser
- **Django REST Framework**: Visit endpoints with `/` at the end for browsable API

## 🔑 Authentication Notes
- Most endpoints require authentication using Token authentication
- Include `Authorization: Token <your_token>` in request headers
- Obtain token by logging in via `/api/accounts/login/`
- Users can only modify their own posts and comments