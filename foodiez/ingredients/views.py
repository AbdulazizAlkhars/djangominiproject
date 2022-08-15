from django.shortcuts import render
from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
# Create your views here.


def home(request):
    ingredients = models.Ingredient.objects.all()
    context = {
        'ingredients': ingredients
    }
    return render(request, 'ingredients/home.html', context)


class IngredientListView(ListView):
    model = models.Ingredient
    template_name = 'ingredients/home.html'
    context_object_name = 'ingredients'


class IngredientDetailView(DetailView):
    model = models.Ingredient
    template_name = 'ingredients/ingredient_detail.html'


class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = models.Ingredient
    fields = ['title', 'description']
    template_name = 'ingredients/ingredient_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class IngredientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Ingredient
    fields = ['title', 'description']
    template_name = 'ingredients/ingredient_form.html'

    def test_func(self):
        ingredient = self.get_object()
        if self.request.user == ingredient.author:
            return True
        return False

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class IngredientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Ingredient
    success_url = reverse_lazy('ingredients-home')
    template_name = 'ingredients/ingredient_confirm_delete.html'

    def test_func(self):
        ingredient = self.get_object()
        if self.request.user == ingredient.author:
            return True
        return False


def about(request):
    return render(request, 'ingredients/about.html', {'title': 'About us page'})
