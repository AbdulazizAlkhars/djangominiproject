from django.urls import path
from . import views


urlpatterns = [
    path('ingredient-list/', views.IngredientListView.as_view(),
         name='ingredients-home'),
    path('ingredient/create/', views.IngredientCreateView.as_view(),
         name='ingredients-create'),
    path('ingredient/<int:pk>/',
         views.IngredientDetailView.as_view(), name='ingredients-detail'),
    path('ingredient/<int:pk>/update/',
         views.IngredientUpdateView.as_view(), name='ingredients-update'),
    path('ingredient/<int:pk>/delete/',
         views.IngredientDeleteView.as_view(), name='ingredients-delete'),
    path('about-ingredient/', views.about, name='ingredients-about'),
]
