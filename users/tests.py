from django.test import TestCase

from recipes.models import Recipe
from .models import User


class UserTestCase(TestCase):
    def test_creates_user_record_in_db(self):
        user = User.objects.create(username="testuser")
        self.assertIsInstance(user, User)

    def test_returns_correct_recipes_count_for_a_user(self):
        user1 = User.objects.create(username="testuser1")
        user2 = User.objects.create(username="testuser2")

        Recipe.objects.create(title="Test Recipe", description="Test Recipe Description", creator=user1)

        self.assertEqual(user1.recipes_count(), 1)
        self.assertEqual(user2.recipes_count(), 0)
