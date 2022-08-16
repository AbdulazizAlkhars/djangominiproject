"""foodiez URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views

# good use of built in views for use auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('foodrecipies.urls')),
    # there can only be one "" route, each one would have to be path('something/', include(<app>.urls))
    # and also check out namespaces in the docs to better help navigate between multiple apps and routes
    path('', include('catagories.urls')),
    path('', include('ingredients.urls')),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"),
         name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"),
         name='user-logout'),
    path('profile/', user_views.profile, name='user-profile'),

]
# there is an issue when navigating your application, it seems that all the functionality is here but there wasn't a clear plan during implementation
# hence why a wireframe is needed
# you seem to have an issue whereby you feel you need more than 1 base.html, you can access it by refering to the app then the template, e.g <appname>/base.html
# or, you could have a templates folder in the root of your application, similar to how we create a media folder, and place the base.html there. this might help with the navigation issues your having
# every app has an about view? why not put that here and have a template, like in a commonly accessible folder like my earlier comment regard base.html?