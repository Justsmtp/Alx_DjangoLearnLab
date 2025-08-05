### API Endpoints - Book Views

- GET `/api/books/` - List all books
- GET `/api/books/<id>/` - Retrieve book by ID
- POST `/api/books/create/` - Create a book (auth required)
- PUT `/api/books/<id>/update/` - Update a book (auth required)
- DELETE `/api/books/<id>/delete/` - Delete a book (auth required)

Permissions:
- Read operations are public
- Write operations require authentication

### 🔍 Filtering, Searching & Ordering

You can filter, search, and sort books using query parameters:

- **Filter** by title, author name, or publication year:
  `/api/books/?title=1984&publication_year=1949`

- **Search** by keyword:
  `/api/books/?search=harari`

- **Order** by fields:
  `/api/books/?ordering=title` (A–Z)
  `/api/books/?ordering=-publication_year` (Newest first)
