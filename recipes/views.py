from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe, Country
from .forms import RecipeForm
from django.urls import reverse_lazy
from django.db.models import Q
    

def CountryView(request, choice):
    """
    Retrieve the country object form the country model
    Retrieve the matching recipe post from the recipe model
    Render countries template with the requested recipes
    """

    # Get the query using q for case insensitive search
    query = Q(name__iexact=choice.capitalize()) | Q(name__iexact=choice.replace("-", " "))
    
    country = get_object_or_404(Country, query)

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
    
    def get_context_data(self, **kwargs):
        """
        Add url data to the context data
        """
        context = super().get_context_data(**kwargs)
        context['url_name'] = self.request.resolver_match.url_name
        return context


# Adapted from 'I think therefore i blog'
class PostLike(View):
    def post(self, request, pk):
        post = get_object_or_404(Recipe, pk=pk)
        if post.likes.filter(id=request.user.pk).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('recipe-detail', args=[pk]))

# Adapted from 'I think therefore i blog'
class PostDislike(View):
    def post(self, request, pk):
        post = get_object_or_404(Recipe, pk=pk)
        if post.dislikes.filter(id=request.user.pk).exists():
            post.dislikes.remove(request.user)
        else:
            post.dislikes.add(request.user)
        return HttpResponseRedirect(reverse('recipe-detail', args=[pk]))


class RecipeDetails(View):
    """ 
    Displays more details of a specific recipe
    Render the boolean True if recipe is liked
    """
    def get(self, request, pk, *args, **kwargs):
        queryset = Recipe.objects
        recipe = get_object_or_404(queryset, pk=pk)
        liked = False
        disliked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        if recipe.dislikes.filter(id=self.request.user.id).exists():
            disliked = True
        return render(
            request, 'details.html', {
                'recipe': recipe,
                'liked': liked,
                'disliked': disliked,
            },
        )


class RecipeView(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(post_approved=True).order_by('-date_created')
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        """
        Add url data and country list to the context data
        """
        context = super().get_context_data(**kwargs)
        context['url_name'] = self.request.resolver_match.url_name
        context['country_list'] = Country.objects.all()
        return context


