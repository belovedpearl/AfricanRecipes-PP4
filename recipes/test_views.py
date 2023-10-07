from django.test import TestCase, Client
from .models import Recipe, Country
from django.urls import reverse
from django.contrib.auth.models import User


class TestViews(TestCase):
    def test_correct_landing_page_used(self):
        """
        Test home page renders correctly
        Test that right template is used
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def setUp(self):
        # Create a setup test user and country
        self.user = User.objects.create_user(username='Test User', password='Test Password')
        self.country = Country.objects.create(name='Test Country')

        # Setup a test recipe
        self.recipe = Recipe.objects.create(
           title='Test Recipe',
           author=self.user,
           ingredients='Test ingredients',
           instructions='Test instructions',
           recipe_image='test_image.png',
           cook_time=120,
           country=self.country,
        )

    def test_get_view_details_page(self):
        """
        Test if details page renders correctly
        Test for the content of the response, assumes user has not liked or disliked the page
        """
        client = Client()

        # Sigin the user
        client.login(username='Test User', password='Test Password')
        url = reverse('recipe-detail', args=[self.recipe.pk])

        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'details.html')

        # Check the content of the response
        self.assertEqual(response.context['recipe'], self.recipe)
        self.assertFalse(response.context['liked'])
        self.assertFalse(response.context['disliked'])

   











