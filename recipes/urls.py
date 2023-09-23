from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeView.as_view(), name='home'),
    path('details/<int:pk>', views.RecipeDetails.as_view(), name='recipe-detail'),
    path('addrecipe/', views.AddRecipe.as_view(), name='add_recipe'),
    path('updaterecipe/edit/<int:pk>', views.UpdateRecipe.as_view(), name='updaterecipe'),
    path('details/<int:pk>/delete', views.DeleteRecipe.as_view(), name='deleterecipe'),
    path('countries/<str:choice>/', views.CountryView, name='countries'),
]