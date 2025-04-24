# accounts/urls.py
from django.urls import path
from . import views  # Correctly import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('manage/', views.user_manage, name='user_manage'),
]
