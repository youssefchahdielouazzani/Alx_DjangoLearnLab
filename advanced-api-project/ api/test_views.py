from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Book
from django.contrib.auth.models import User


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create user and login
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")

        # Sample data
        self.book1 = Book.objects.create(
            title="Alpha Book",
            author="Author A",
            publication_year=2000
        )

        self.book2 = Book.objects.create(
            title="Beta Book",
            author="Author B",
            publication_year=2010
        )

    # GET LIST
    def test_get_books_list(self):
        url = reverse("books-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # CREATE BOOK
    def test_create_book(self):
        url = reverse("books-list")
        data = {
            "title": "New Book",
            "author": "New Author",
            "publication_year": 2022
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, "New Book")

    # UPDATE BOOK
    def test_update_book(self):
        url = reverse("books-detail", args=[self.book1.id])
        data = {
            "title": "Updated Alpha",
            "author": self.book1.author,
            "publication_year": self.book1.publication_year
        }

        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Alpha")

    # DELETE BOOK
    def test_delete_book(self):
        url = reverse("books-detail", args=[self.book1.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # FILTER
    def test_filter_books_by_title(self):
        url = reverse("books-list") + "?title=Alpha"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # SEARCH
    def test_search_books(self):
        url = reverse("books-list") + "?search=Alpha"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Alpha Book")

    # ORDERING
    def test_order_books(self):
        url = reverse("books-list") + "?ordering=title"
        response = self.client.get(url)

        titles = [book["title"] for book in response.data]

        self.assertEqual(titles, ["Alpha Book", "Beta Book"])

