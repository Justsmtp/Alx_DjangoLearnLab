from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

        self.author = Author.objects.create(name='George Orwell')
        self.book1 = Book.objects.create(title='1984', publication_year=1949, author=self.author)
        self.book2 = Book.objects.create(title='Animal Farm', publication_year=1945, author=self.author)

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        url = reverse('book-create')
        data = {
            'title': 'Homage to Catalonia',
            'publication_year': 1938,
            'author': self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_retrieve_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], '1984')

    def test_update_book(self):
        url = reverse('book-update', kwargs={'pk': self.book1.pk})
        data = {
            'title': 'Nineteen Eighty-Four',
            'publication_year': 1949,
            'author': self.author.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Nineteen Eighty-Four')

    def test_delete_book(self):
        url = reverse('book-delete', kwargs={'pk': self.book2.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_title(self):
        url = reverse('book-list') + '?title=1984'
        response = self.client.get(url)
        titles = [book['title'] for book in response.data]
        self.assertIn('1984', titles)
        self.assertNotIn('Animal Farm', titles)
        self.assertEqual(titles.count('1984'), 1)

    def test_search_books(self):
        url = reverse('book-list') + '?search=animal'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book['title'] for book in response.data]
        self.assertIn('Animal Farm', titles)

    def test_order_books_by_year(self):
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))