from django.contrib import admin
from .models import Recipe, Country
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    Specifies how the admin panel is displayed
    Allows the use of summernote editor for selected field
    """
    list_display = ('id', 'title', 'post_approved', 'date_created')
    search_fields = ['title', 'cook_time', 'country'] 
    list_filter = ('date_created', 'post_approved', 'country')
    summernote_fields = ('ingredients', 'instructions')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
