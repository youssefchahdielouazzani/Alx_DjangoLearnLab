from django.test import TestCase
from rest_framework.test import APIClient
from accounts.models import CustomUser
from .models import Post

class FeedTestCase(TestCase):
    def setUp(self):
        self.user1 = CustomUser.objects.create_user(username='user1', password='pass')
        self.user2 = CustomUser.objects.create_user(username='user2', password='pass')
        self.post = Post.objects.create(author=self.user2, content="Hello feed!")
        self.user1.following.add(self.user2)
        self.client = APIClient()
        self.client.login(username='user1', password='pass')

    def test_feed(self):
        response = self.client.get('/posts/feed/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['content'], "Hello feed!")


