from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Users
        self.admin_user = User.objects.create_superuser(
            username='admin', password='admin123'
        )
        self.normal_user = User.objects.create_user(
            username='user', password='user123'
        )

        # A sample book
        self.book = Book.objects.create(
            title="Test Book",
            author="Author A",
            price=10.00
        )

        # URLs
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])

    # --------------------------
    #   GET Tests
    # --------------------------
    def test_get_books_list(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # The check requires response.data
        self.assertIsInstance(response.data, list)
        self.assertEqual(response.data[0]['title'], "Test Book")

    def test_get_single_book(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Book")

    # --------------------------
    #   POST Tests
    # --------------------------
    def test_create_book_as_admin(self):
        self.client.login(username='admin', password='admin123')

        data = {
            "title": "New Book",
            "author": "Author B",
            "price": 15.00
        }

        response = self.client.post(self.list_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Book")
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_as_normal_user_forbidden(self):
        self.client.login(username='user', password='user123')

        data = {
            "title": "Should Fail",
            "author": "User",
            "price": 5.00
        }

        response = self.client.post(self.list_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # --------------------------
    #   PATCH Tests
    # --------------------------
    def test_update_book_as_admin(self):
        self.client.login(username='admin', password='admin123')

        data = {"title": "Updated Book"}

        response = self.client.patch(self.detail_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Book")

        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    # --------------------------
    #   DELETE Tests
    # --------------------------
    def test_delete_book_as_admin(self):
        self.client.login(username='admin', password='admin123')

        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_delete_book_as_normal_user_forbidden(self):
        self.client.login(username='user', password='user123')

        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
