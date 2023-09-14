from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
import datetime


class Country(models.Model):
    """
    Countries Model
    Orders the countries according to their name
    returns the country's name
    """
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """
    Recipe Model
    Meta put latest post first
    Generate count for the like button
    """
    title = models.CharField(max_length=150, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_posts') 
    ingredients = models.TextField()
    instructions = models.TextField()
    recipe_image = CloudinaryField('recipeimage', default='placeholder')
    cook_time = models.PositiveIntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default='Africa')
    likes = models.ManyToManyField(User, related_name='recipe_like', blank=True)
    dislikes = models.ManyToManyField(User, related_name='recipe_dislike', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True)
    post_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        """
        Returns the URL back home
        """
        return reverse('home')

    def save(self, *args, **kwargs):
        """
        Overide function to date of post update
        """
        if self.id:
            self.date_updated = datetime.datetime.now()
        super().save(*args, **kwargs)
