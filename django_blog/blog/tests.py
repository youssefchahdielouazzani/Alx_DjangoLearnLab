from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

class BlogModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(title='Test Post', content='Test content', author=self.user)

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(str(self.post), 'Test Post')

    def test_comment_creation(self):
        comment = Comment.objects.create(post=self.post, author=self.user, content='Nice post!')
        self.assertEqual(str(comment), f'Comment by {self.user} on {self.post}')
        self.assertEqual(comment.content, 'Nice post!')

