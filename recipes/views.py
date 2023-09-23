from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe, Country
from .forms import RecipeForm
from django.urls import reverse_lazy


def CountryView(request, choice):
    """
    Retrieve the country object form the country model
    Retrieve the matching recipe post from the recipe model
    Render countries template with the requested recipes
    """
    country = get_object_or_404(Country, name=choice.capitalize())
    
    recipe_posts = Recipe.objects.filter(country=country)
    return render(request, 'countries.html', {'choice': country, 'recipe_posts': recipe_posts})


class DeleteRecipe(generic.DeleteView):
    """
    Allows users to delete recipe post
    Renders the deleterecipe form
    """
    model = Recipe
    template_name = "deleterecipe.html"
    success_url = reverse_lazy('home')


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

    def get_context_data(self, *args, **kwargs):
        """
        Retrieve all country list from the data base
        Add country list to the context data for access
        """
        country_list = Country.objects.all()
        context = super(RecipeView, self).get_context_data(*args, **kwargs)
        context['country_list'] = country_list
        return context

