from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Like

class LikeModelTest(TestCase):
    def test_like_creation(self):
        user = User.objects.create_user(username='user1', password='pass')
        post = Post.objects.create(author=user, content='Test post')
        like = Like.objects.create(user=user, post=post)

        self.assertEqual(like.user, user)
        self.assertEqual(like.post, post)

