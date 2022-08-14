from django.urls import path
from foodrecipies import views

urlpatterns = [
    path('', views.home, name='recipes-home'),
    path('about/', views.about, name='recipes-about'),
]
