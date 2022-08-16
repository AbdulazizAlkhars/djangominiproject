from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f"Account created for {username}! Please login")
            return redirect('user-login')
    else:
        form = forms.UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
# I like the effort to use messages, but why redirect the user to the login page? Instead, maybe it would be a better user experience to be logged in and redirected to a more relevant page

@login_required()
def profile(request):
    return render(request, 'users/profile.html')
