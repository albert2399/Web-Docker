from django.test import TestCase
from app.models import Post

class PostTestCase(TestCase):
    def testPost(self):
        post = Post(title="Web-test", description="Test-post", wiki="Post Body")
        self.assertEqual(post.title, "Web-test")
        self.assertEqual(post.description, "Test-post")
        self.assertEqual(post.wiki, "Post Body")
        