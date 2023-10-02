from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeView.as_view(), name='home'),
    path('details/<int:pk>', views.RecipeDetails.as_view(), name='recipe-detail'),
    path('addrecipe/', views.AddRecipe.as_view(), name='add_recipe'),
    path('updaterecipe/edit/<int:pk>', views.UpdateRecipe.as_view(), name='updaterecipe'),
    path('details/<int:pk>/delete', views.DeleteRecipe.as_view(), name='deleterecipe'),
    path('countries/<str:choice>/', views.CountryView, name='countries'),
    path('like/<int:pk>', views.PostLike.as_view(), name='recipe_like'),
    path('dislike/<int:pk>', views.PostDislike.as_view(), name='recipe_dislike'),
    path('edit_profile/', views.EditUserView.as_view(), name='edit_profile'),
    path('password/', views.ChangePasswordView.as_view(template_name='change_password.html')),
    path('password_changed/', views.password_changed, name='password_changed')

]