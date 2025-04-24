from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from comments.models import Comment
from django.contrib.auth import logout

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')




@login_required
def user_manage(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'delete_comments':
            Comment.objects.filter(user=request.user).delete()
        elif action == 'delete_account':
            user = request.user           # Store the user object first
            logout(request)               # Log out (clears session)
            user.delete()                 # Now delete the user object
        return redirect('login')
    return redirect('login')