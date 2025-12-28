from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def test_create_post(self):
        post = Post.objects.create(
            title='Test Post',
            content='Test content'
        )
        self.assertEqual(post.title, 'Test Post')

