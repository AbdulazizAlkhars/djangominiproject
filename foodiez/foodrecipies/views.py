from django.shortcuts import render, HttpResponse
from . import models
recipes = [
    {
        'author': 'John Doe',
        'title': 'Spaghetti Carbonara',
        'directions': 'Cook the spaghetti and the Carbonara',
        'date_posted': 'May 28, 2022',
    },
    {
        'author': 'Jane Doe',
        'title': 'Pizza',
        'directions': 'Cook the pizza',
        'date_posted': 'May 15, 2021',
    },
    {
        'author': 'Joe Smith',
        'title': 'Pasta',
        'directions': 'Cook the pasta',
        'date_posted': 'May 1, 2020',
    }
]

# Create your views here.


def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'recipes/home.html', context)


def about(request):
    return render(request, 'recipes/about.html', {'title': 'About us page'})
