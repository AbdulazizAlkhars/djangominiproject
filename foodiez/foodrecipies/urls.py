from django.urls import path
from . import views


urlpatterns = [
    path('recipe-list/', views.RecipeListView.as_view(), name='recipes-home'),
    path('recipe/create/', views.RecipeCreateView.as_view(), name='recipes-create'),
    path('recipe/<int:pk>/',
         views.RecipeDetailView.as_view(), name='recipes-detail'),
    path('recipe/<int:pk>/update/',
         views.RecipeUpdateView.as_view(), name='recipes-update'),
    path('recipe/<int:pk>/delete/',
         views.RecipeDeleteView.as_view(), name='recipes-delete'),
    path('about-recipe/', views.about, name='recipes-about'),
]
