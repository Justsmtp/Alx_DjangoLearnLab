# blog/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'blog'

urlpatterns = [
    # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),

    # Blog post URLs
    path('', views.PostListView.as_view(), name='home'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/new/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    # Comment URLs
    path('post/<int:post_id>/comments/new/', views.add_comment, name='comment_create'),
    path('comment/<int:comment_id>/update/', views.edit_comment, name='comment_update'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='comment_delete'),
]
