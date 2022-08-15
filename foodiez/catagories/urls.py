from django.urls import path
from . import views


urlpatterns = [
    path('', views.CatagoryListView.as_view(), name='catagories-home'),
    path('catagory/create/', views.CatagoryCreateView.as_view(),
         name='catagories-create'),
    path('catagory/<int:pk>/',
         views.CatagoryDetailView.as_view(), name='catagories-detail'),
    path('catagory/<int:pk>/update/',
         views.CatagoryUpdateView.as_view(), name='catagories-update'),
    path('catagory/<int:pk>/delete/',
         views.CatagoryDeleteView.as_view(), name='catagories-delete'),
    path('about/', views.about, name='catagories-about'),
]
