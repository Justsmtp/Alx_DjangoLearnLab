📝 Django Blog Post CRUD Documentation
📌 Overview
This project implements CRUD (Create, Read, Update, Delete) functionality for blog posts using Django.
It allows:

Visitors to view blog posts.

Authenticated users to create new posts.

Authors to edit and delete their own posts.

The project also includes user registration, login/logout, and profile management.

⚙️ Features Implemented
CRUD Operations
Create – Authenticated users can create new blog posts.

Read – Any user (authenticated or not) can view a list of blog posts or a single post.

Update – Only the author of a post can edit it.

Delete – Only the author of a post can delete it.

Additional
User Authentication (register, login, logout)

User Profile Management

Permissions and Access Control

Responsive Templates with Bootstrap

🛠 Tech Stack
Backend: Django

Frontend: HTML, CSS (Bootstrap)

Database: SQLite (default, can be swapped with PostgreSQL/MySQL)

Authentication: Django’s built-in auth system

📂 File Structure (Relevant Parts)
arduino

blog/
│
├── templates/
│   ├── blog/
│   │   ├── home.html
│   │   ├── post_detail.html
│   │   ├── post_form.html
│   │   ├── post_confirm_delete.html
│   ├── registration/
│       ├── login.html
│       ├── logout.html
│       ├── register.html
│   ├── profile.html
│
├── models.py
├── forms.py
├── views.py
├── urls.py
🚀 CRUD Flow
1️⃣ Create a Post
URL: /post/new/

View: PostCreateView

Template: post_form.html

Permissions: Must be logged in.

Process:

User fills in title and content.

Author is automatically set to the logged-in user.

Redirects to the newly created post's detail page.

2️⃣ Read Posts
List View

URL: /

View: PostListView

Template: home.html

Shows all posts ordered by creation date (newest first).

Detail View

URL: /post/<id>/

View: PostDetailView

Template: post_detail.html

Shows full content of a single post.

3️⃣ Update a Post
URL: /post/<id>/update/

View: PostUpdateView

Template: post_form.html

Permissions: Must be logged in and must be the post author.

4️⃣ Delete a Post
URL: /post/<id>/delete/

View: PostDeleteView

Template: post_confirm_delete.html

Permissions: Must be logged in and must be the post author.

🔒 Permissions
Create: Authenticated users only.

Update/Delete: Only the post's author.

Read: Everyone.

Implementation uses:

python

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
🧪 Testing Checklist
✅ Registration works and logs user in automatically
✅ Users can log in and log out
✅ Post creation is restricted to logged-in users
✅ Only authors can update or delete their posts
✅ Anonymous users can view posts but cannot create, edit, or delete
✅ Navigation links work correctly between pages

🖥 Running the Project
Clone the repository

```bash

git clone <repo-url>
cd django_blog
Install dependencies

```bash

pip install -r requirements.txt
Apply migrations

```bash

python manage.py migrate
Create superuser (optional)

```bash

python manage.py createsuperuser
Run the development server

```bash

python manage.py runserver
Open in browser

```bash

http://127.0.0.1:8000/
📄 License
This project is open source. Feel free to use and modify.