from .models import Recipe
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'author', 'country', 'ingredients', 'instructions', 'cook_time', 'recipe_image')

    def __init__(self, *args, **kwargs):
        """
        Form helper to generate form fields
        """
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('title', css_class='form-control', placeholder='Recipe Local Name'),
            Field('author', css_class='form-control'),
            Field('country', css_class='form-control'),
            Field('ingredients', css_class='form-control'),
            Field('instructions', css_class='form-control'),
            Field('recipe_image'),
            Field('cook_time', css_class='form-control', style='margin-bottom: 10px;', placeholder='in minutes'),
            Submit('submit', 'Submit', css_class='btn btn-secondary btn-lg', style='margin-bottom: 10px;')
        )