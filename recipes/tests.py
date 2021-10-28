from django.test import TestCase

from users.models import User
from .models import Recipe


class RecipeTestCase(TestCase):
    user = None

    def setUp(self) -> None:
        self.user = User.objects.create(username="testuser", is_active=True)

    def test_creates_recipe_record_in_db(self):
        recipe = Recipe.objects.create(
            title="Test Recipe", description="Description of test recipe", creator=self.user
        )
        self.assertIsInstance(recipe, Recipe)
