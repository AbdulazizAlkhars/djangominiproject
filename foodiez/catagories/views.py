from django.shortcuts import render
from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
# Create your views here.


def home(request):
    catagories = models.Catagory.objects.all()
    context = {
        'catagories': catagories
    }
    return render(request, 'catagories/home.html', context)


class CatagoryListView(ListView):
    model = models.Catagory
    template_name = 'catagories/home.html'
    context_object_name = 'catagories'


class CatagoryDetailView(DetailView):
    model = models.Catagory
    template_name = 'catagories/catagory_detail.html'


class CatagoryCreateView(LoginRequiredMixin, CreateView):
    model = models.Catagory
    fields = ['title', 'description']
    template_name = 'catagories/catagory_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CatagoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Catagory
    fields = ['title', 'description']
    template_name = 'catagories/catagory_form.html'

    def test_func(self):
        catagory = self.get_object()
        if self.request.user == catagory.author:
            return True
        return False

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CatagoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Catagory
    success_url = reverse_lazy('catagories-home')
    template_name = 'catagories/catagory_confirm_delete.html'

    def test_func(self):
        catagory = self.get_object()
        if self.request.user == catagory.author:
            return True
        return False


def about(request):
    return render(request, 'catagories/about.html', {'title': 'About us page'})
