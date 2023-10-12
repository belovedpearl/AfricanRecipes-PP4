from django.test import TestCase
from .forms import RecipeForm, EditProfileForm
from django.contrib.auth.models import User
from django.urls import reverse


class TestItemForm(TestCase):
    def test_recipe_title_is_required(self):
        """
        Test if title field is required
        """
        form = RecipeForm({"title": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors.keys())
        self.assertEqual(form.errors["title"][0], "This field is required.")
    
    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test form fields
        Checks if represented form field is the same as the actual fields 
        """
        form = RecipeForm()
        formfields = ["title", "author", "country","ingredients", "instructions", "cook_time", "recipe_image"]
        actualfield = list(form.fields.keys())
        self.assertEqual(formfields, actualfield)


class TestEditProfileForm(TestCase):
    def test_edit_profile_form_valid_data(self):
        """
        Test edit profile form
        """
        # Create a user instance for testing
        user = User.objects.create_user(username='testuser', password='testpassword')

        # Prepare valid form data
        form_data = {
            'email': 'test@yes.com',
            'first_name': 'Ade',
            'last_name': 'Ola',
            'username': 'newuser',
        }
        form = EditProfileForm(data=form_data, instance=user)
        self.assertTrue(form.is_valid())

    def test_edit_profile_form_invalid_data(self):
        """
        Test form
        Check form validity with empty username fielf 
        """
        # Create a user instance for testing
        user = User.objects.create_user(username='testuser', password='testpassword')

        # Check with empty username
        form_data = {
            'email': 'test@yes.com',
            'first_name': 'Ade',
            'last_name': 'Ola',
            'username': '',
        }
        form = EditProfileForm(data=form_data, instance=user)
        self.assertFalse(form.is_valid())


class EditUserViewTest(TestCase):
    def setUp(self):
        # A representative test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
        )

    def test_successful_form_submission(self):
        """
        Test for successful form submission
        Test page redirect after form submission
        """
        self.client.login(username='testuser', password='testpassword')

        # Redine user's details to submit
        form_data = {
            'username': 'test_user_name',
            'first_name': 'NewFirst Name',
            'last_name': 'NewLast Name',
            'email': 'newemail@yes.com',
        }
        response = self.client.post(reverse('edit_profile'), form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))


