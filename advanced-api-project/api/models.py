from django.db import models
from datetime import datetime

class Author(models.Model):
    """
    The Author model represents a book author.
    Each author can have multiple books (One-to-Many).
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    The Book model represents a book written by an author.
    Each book has a title, publication year, and is linked to an Author.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
