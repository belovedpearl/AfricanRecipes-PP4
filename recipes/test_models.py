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

    def test_recipe_primary_key(self):
        Recipe.objects.create( 
            title='Test Recipe', 
            author=self.user, 
            ingredients='Test ingredients', 
            instructions='Test instructions', 
            recipe_image='test_image.png', 
            cook_time=120, 
            country=self.country,)
        recipe = Recipe.objects.get(title='Test Recipe')
        self.assertIsNotNone(recipe.pk)
        self.assertIsInstance(recipe.pk, int)
        expected_pk = 1
        self.assertEqual(recipe.pk, expected_pk)

    def test_recipe_title_max_length(self):
        Recipe.objects.create( 
            title='Test Recipe', 
            author=self.user, 
            ingredients='Test ingredients', 
            instructions='Test instructions', 
            recipe_image='test_image.png', 
            cook_time=120, 
            country=self.country,)
        recipe = Recipe.objects.get(pk=1)
        max_length = recipe._meta.get_field('title').max_length
        self.assertEqual(max_length, 150)

    def test_recipe_like_and_dislike(self):
        # Create users to test for likes and dislikes
        user1 = User.objects.create_user(username='user1', password='password1')
        user2 = User.objects.create_user(username='user2', password='password2')
        recipe = Recipe.objects.create(
            title='Test Recipe',
            author=self.user,
            ingredients='Test ingredients',
            instructions='Test instructions',
            recipe_image='test_image.jpg',
            cook_time=30,
            country=self.country,
        )
        recipe.likes.add(user1)
        self.assertTrue(recipe.likes.filter(pk=user1.pk).exists())
        self.assertFalse(recipe.likes.filter(pk=user2.pk).exists())

        recipe.dislikes.add(user2)
        self.assertTrue(recipe.dislikes.filter(pk=user2.pk).exists())
        self.assertFalse(recipe.dislikes.filter(pk=user1.pk).exists())


            