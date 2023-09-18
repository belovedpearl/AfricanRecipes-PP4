from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeView.as_view(), name='home'),
    path('details/<int:pk>', views.RecipeDetails.as_view(), name='recipe-detail'),
    
]