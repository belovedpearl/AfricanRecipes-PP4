from .models import Recipe
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            "title",
            "country",
            "ingredients",
            "instructions",
            "cook_time",
            "recipe_image",
        )
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Recipe Local Name",
                }
            ),
            "country": forms.Select(attrs={"class": "form-control"}),
            "ingredients": SummernoteWidget(attrs={"class": "form-control"}),
            "instructions": SummernoteWidget(attrs={"class": "form-control"}),
            "cook_time": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "style": "margin-bottom: 10px;",
                    "placeholder": "in minutes",
                }
            ),
        }


class EditProfileForm(forms.ModelForm):
    """
    Edit choice fields in the user detail
    """

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class ChangePasswordForm(PasswordChangeForm):
    """
    Create form for user's password change
    """

    old_password = forms.CharField(
        max_length=100, widget=forms.PasswordInput(attrs={"type": "password"})
    )
    new_password1 = forms.CharField(
        max_length=100, widget=forms.PasswordInput(attrs={"type": "password"})
    )
    new_password2 = forms.CharField(
        max_length=100, widget=forms.PasswordInput(attrs={"type": "password"})
    )

    class Meta:
        """
        Choose model to use
        Displays fields in order shown
        """

        model = User
        fields = ("old_password", "new_password1", "new_password2")
