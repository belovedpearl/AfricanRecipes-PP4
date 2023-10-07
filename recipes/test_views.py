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

   











