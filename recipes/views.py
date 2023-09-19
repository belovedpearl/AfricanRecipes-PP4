from django.shortcuts import render
from django.views import generic
from .models import Recipe
from .forms import RecipeForm


class UpdateRecipe(generic.UpdateView):
    """
    Retrieves the recipe instance to be updated
    Uses the model recipe and RecipeForm
    """
    model = Recipe
    template_name = "updaterecipe.html"
    form_class = RecipeForm


class AddRecipe(generic.CreateView):
    """
    Renders page to add recipe
    Allows user submit a new recipe
    """
    model = Recipe
    form_class = RecipeForm
    template_name = "addrecipe.html"
    


class RecipeDetails(generic.DetailView,):
    """
    Displays more details of a specific recipe
    """
    model = Recipe
    template_name = "details.html"


class RecipeView(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(post_approved=True).order_by('-date_created')
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        """
        Add url data to the context data
        """
        context = super().get_context_data(**kwargs)
        context['url_name'] = self.request.resolver_match.url_name
        return context


