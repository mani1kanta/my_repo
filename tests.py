from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

class YourAppTestCase(TestCase):
    def setUp(self):
        # Set up test data
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=self.user,
            category='Test Category'
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            content='This is a test comment.'
        )

    def test_post_model(self):
        # Test the Post model
        post = Post.objects.get(id=self.post.id)
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.author, self.user)

    def test_comment_model(self):
        # Test the Comment model
        comment = Comment.objects.get(id=self.comment.id)
        self.assertEqual(comment.content, 'This is a test comment')
        self.assertEqual(comment.author, self.user)

    def test_post_view(self):
        # Test views (if applicable)
        response = self.client.get('/your-app-url/')  # Replace with the actual URL
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on your view's behavior

    # Add more tests as needed
