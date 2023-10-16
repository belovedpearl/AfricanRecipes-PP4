from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe, Country
from .forms import RecipeForm, EditProfileForm, ChangePasswordForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    """
    Chooses custom form to use
    Redirect to edit_profile page
    """

    form_class = ChangePasswordForm
    success_url = reverse_lazy("edit_profile")
    success_message = "Your Password was changed successfully"

    def get_context_data(self, **kwargs):
        """
        Add country list to the context data
        """
        context = super().get_context_data(**kwargs)
        context["country_list"] = Country.objects.all()
        return context


class EditUserView(SuccessMessageMixin, generic.UpdateView):
    """
    Allow user edit profile using the editprofile form
    Render form using edit_profile page
    redirect back home
    """

    form_class = EditProfileForm
    template_name = "edit_profile.html"
    success_url = reverse_lazy("home")
    success_message = "Your Profile was successfully updated"

    def get_object(self):
        """
        Return current log in in user
        """
        return self.request.user

    def get_context_data(self, **kwargs):
        """
        Add country list to the context data
        """
        context = super().get_context_data(**kwargs)
        context["country_list"] = Country.objects.all()
        return context


def CountryView(request, choice):
    """
    Retrieve the country object form the country model
    Retrieve the matching recipe post from the recipe model
    Render countries template with the requested recipes
    """

    # Get the query using q for case insensitive search
    # (source: https://docs.djangoproject.com/en/dev/ref/models/querysets/#iexact)
    query = Q(name__iexact=choice.capitalize()) | Q(
        name__iexact=choice.replace("-", " ")
    )

    country = get_object_or_404(Country, query)

    country_list = Country.objects.all()

    recipe_posts = Recipe.objects.filter(country=country)
    return render(
        request,
        "countries.html",
        {"choice": country, "recipe_posts": recipe_posts, "country_list": country_list},
    )


class DeleteRecipe(SuccessMessageMixin, generic.DeleteView):
    """
    Allows users to delete recipe post
    Renders the deleterecipe form
    """

    model = Recipe
    template_name = "deleterecipe.html"
    success_url = reverse_lazy("home")
    success_message = "Recipe successfully deleted"

    # Source: https://stackoverflow.com/questions/47636968/django-messages-for-a-successfully-delete-add-or-edit-item
    def delete(self, request, *args, **kwargs):
        """
        Confirms to user the deletion of a recipe
        """
        messages.warning(self.request, self.success_message)
        return super(DeleteRecipe, self).delete(request, *args, **kwargs)


class UpdateRecipe(SuccessMessageMixin, generic.UpdateView):
    """
    Retrieves the recipe instance to be updated
    Uses the model recipe and RecipeForm
    Alert the user if successfully updated
    """

    model = Recipe
    template_name = "updaterecipe.html"
    form_class = RecipeForm
    success_message = "%(title)s was updated successfully"

    def get_context_data(self, **kwargs):
        """
        Add country list to the context data
        """
        context = super().get_context_data(**kwargs)
        context["country_list"] = Country.objects.all()
        return context


class AddRecipe(generic.CreateView):
    """
    Renders page to add recipe
    Allows user submit a new recipe
    """

    model = Recipe
    form_class = RecipeForm
    template_name = "addrecipe.html"
    success_url = reverse_lazy("home")

    # Source: https://stackoverflow.com/questions/28723266/django-display-message-after-post-form-submit
    def form_valid(self, form):
        """
        Display message confirming recipe submission to users
        """
        messages.success(self.request, "Recipe added successfully! Awaiting Approval.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """
        Add url data to the context data
        """
        context = super().get_context_data(**kwargs)
        context["url_name"] = self.request.resolver_match.url_name
        context["country_list"] = Country.objects.all()
        return context


# Adapted from 'I think therefore i blog'
class PostLike(View):
    """
    Handles post request
    Fetch the recipe object
    Toggles like
    Redirect to recipe-detail page
    """

    def post(self, request, pk):
        post = get_object_or_404(Recipe, pk=pk)
        if post.likes.filter(id=request.user.pk).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
            if post.dislikes.filter(id=request.user.pk).exists():
                post.dislikes.remove(request.user)
        return HttpResponseRedirect(reverse("recipe-detail", args=[pk]))


# Adapted from 'I think therefore i blog'
class PostDislike(View):
    """
    Handles post request
    Fetch the recipe object
    Toggles dislike
    Redirect to recipe-detail page
    """

    def post(self, request, pk):
        post = get_object_or_404(Recipe, pk=pk)
        if post.dislikes.filter(id=request.user.pk).exists():
            post.dislikes.remove(request.user)
        else:
            post.dislikes.add(request.user)
            if post.likes.filter(id=request.user.pk).exists():
                post.likes.remove(request.user)
        return HttpResponseRedirect(reverse("recipe-detail", args=[pk]))


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
        # Get the country list
        country_list = Country.objects.all()

        return render(
            request,
            "details.html",
            {
                "recipe": recipe,
                "liked": liked,
                "disliked": disliked,
                "country_list": country_list,
            },
        )


class RecipeView(generic.ListView):
    """
    Uses the Recipe model
    Defines the queryset
    Recder the index page
    """

    model = Recipe
    queryset = Recipe.objects.filter(post_approved=True).order_by("-date_created")
    template_name = "index.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        """
        Add url data and country list to the context data
        """
        context = super().get_context_data(**kwargs)
        context["url_name"] = self.request.resolver_match.url_name
        context["country_list"] = Country.objects.all()
        return context


def error_404(request, exception):
    """
    Handles HTTP 404 Page Not Found errors
    """
    template_name = "error_404.html"
    return render(request, template_name)


def error_500(request):
    """
    Handles HTTP 500 Server Error errors
    """
    template_name = "500.html"
    return render(request, template_name)
