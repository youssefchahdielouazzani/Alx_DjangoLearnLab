from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Post, Like

class LikePostTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='pass')
        self.user2 = User.objects.create_user(username='user2', password='pass')
        self.post = Post.objects.create(author=self.user1, content='Test Post')
        self.client = APIClient()
        self.client.login(username='user2', password='pass')

    def test_like_post(self):
        response = self.client.post(f'/posts/{self.post.id}/like/')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Like.objects.count(), 1)

    def test_unlike_post(self):
        self.client.post(f'/posts/{self.post.id}/like/')
        response = self.client.post(f'/posts/{self.post.id}/unlike/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Like.objects.count(), 0)

