from django.test import TestCase
from .models import Recipe, Country
from django.contrib.auth.models import User


class TestModel(TestCase):
    def setUp(self):
        # Add a placeholder user and country
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.country = Country.objects.create(name='test_country')

    def test_recipe_creation(self):
        # Test for complete recipe creation
        recipe = Recipe.objects.create(
            title='Test Recipe',
            author=self.user,
            ingredients='Test ingredients',
            instructions='Test instructions',
            recipe_image='test_image.png',
            cook_time=120,
            country=self.country,
        )
        # Check for successful recipe creation
        self.assertEqual(recipe.title, 'Test Recipe')
        self.assertEqual(recipe.author, self.user)
        self.assertEqual(recipe.ingredients, 'Test ingredients')
        self.assertEqual(recipe.instructions, 'Test instructions')
        self.assertEqual(recipe.recipe_image, 'test_image.png')
        self.assertEqual(recipe.cook_time, 120)
        self.assertEqual(recipe.country, self.country)
    