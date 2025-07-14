import os
import django

# Setup environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author = Author.objects.get(name='Chinua Achebe')
books_by_author = author.books.all()
print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

# 2. List all books in a library
library = Library.objects.get(name='Central Library')
library_books = library.books.all()
print(f"Books in {library.name}: {[book.title for book in library_books]}")

# 3. Retrieve the librarian for a library
librarian = library.librarian
print(f"Librarian of {library.name}: {librarian.name}")
