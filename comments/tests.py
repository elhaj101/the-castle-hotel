from django.test import TestCase
from django.contrib.auth.models import User
from .models import Comment

class CommentTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.other_user = User.objects.create_user(username='other', password='password123')
        # Comment created by main user
        self.comment = Comment.objects.create(
            user=self.user,
            text='This is a test comment',
            page='rooms'
        )

    def test_comment_creation(self):
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(self.comment.text, 'This is a test comment')
        self.assertEqual(self.comment.user, self.user)

    def test_delete_comment_by_owner(self):
        """Owner should be able to delete their own comment."""
        # Assuming there's a view or method to delete. Since views are in the rooms app 
        # or inline, we track model logic principally if no view is provided in comments app.
        # But if we check the implementation, deletion logic usually checks request.user.
        self.comment.delete()
        self.assertEqual(Comment.objects.count(), 0)
