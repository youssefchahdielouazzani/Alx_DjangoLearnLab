from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Like

class PostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        self.post = Post.objects.create(author=self.user, content='Test post')

    def test_like_post(self):
        like = Like.objects.create(post=self.post, user=self.user)
        self.assertEqual(self.post.likes.count(), 1)


