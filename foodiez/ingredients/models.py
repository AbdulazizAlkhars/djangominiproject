from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from catagories.models import Catagory
# Create your models here.


class Ingredient(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    catagory = models.ForeignKey(
        Catagory, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('ingredients-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
