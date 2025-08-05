### API Endpoints - Book Views

- GET `/api/books/` - List all books
- GET `/api/books/<id>/` - Retrieve book by ID
- POST `/api/books/create/` - Create a book (auth required)
- PUT `/api/books/<id>/update/` - Update a book (auth required)
- DELETE `/api/books/<id>/delete/` - Delete a book (auth required)

Permissions:
- Read operations are public
- Write operations require authentication
