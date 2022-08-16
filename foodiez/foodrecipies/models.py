from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from catagories.models import Catagory 
from ingredients.models import Ingredient
# Create your models here.


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    catagory = models.ManyToManyField(Ingredient) # there seems to be confusion with regards to this field, shouldnt we have this field called ingredients?
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # what about linking the ingredients to the recipe in one field?
    # not having an ERD on hand, even if changes were made on the fly, will cause issues such as this to arise
    
    def get_absolute_url(self):
        return reverse('recipes-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
