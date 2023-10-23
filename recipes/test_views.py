from django.test import TestCase, Client
from .models import Recipe, Country
from django.urls import reverse
from django.contrib.auth.models import User


class TestViews(TestCase):
    def setUp(self):
        # Create a setup test user and country
        self.user = User.objects.create_user(
            username="Test User", password="Test Password"
        )
        self.country = Country.objects.create(name="Test Country")

        # Setup a test recipe
        self.recipe = Recipe.objects.create(
            title="Test Recipe",
            author=self.user,
            ingredients="Test ingredients",
            instructions="Test instructions",
            recipe_image="test_image.png",
            cook_time=120,
            country=self.country,
        )

    def test_correct_landing_page_used(self):
        """
        Test home page renders correctly
        Test that right template is used
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_get_view_details_page(self):
        """
        Test if details page renders correctly
        Test for the content of the response,
        Assumes user has not liked or disliked the page
        """
        client = Client()

        # Sigin the user
        client.login(username="Test User", password="Test Password")
        url = reverse("recipe-detail", args=[self.recipe.pk])

        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "details.html")

        # Check the content of the response
        self.assertEqual(response.context["recipe"], self.recipe)
        self.assertFalse(response.context["liked"])
        self.assertFalse(response.context["disliked"])

    def test_get_add_recipe_page(self):
        """
        Test if add_recipe page renders correctly
        """
        response = self.client.get("/addrecipe/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "addrecipe.html")

    def test_get_update_recipe_page(self):
        """
        Test if update recipe page renders correctly
        """
        url = reverse("updaterecipe", kwargs={"pk": self.recipe.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "updaterecipe.html")

    def test_get_delete_recipe_page(self):
        """
        Test if delete recipe page renders correctly
        """
        url = reverse("deleterecipe", kwargs={"pk": self.recipe.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "deleterecipe.html")

    def test_get_country_page(self):
        """
        Test country page renders succesfully
        """
        url = reverse("countries", kwargs={"choice": "Test Country"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "countries.html")

    def test_get_edit_user_page(self):
        """
        Test if edit user page renders correctly
        """
        self.client.login(username="Test User", password="Test Password")
        url = reverse("edit_profile")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "edit_profile.html")
