from django.urls import path
from . import views
from comments.views import add_comment

urlpatterns = [
    path('', views.restaurant_list, name='restaurant_list'),
    path('comment/add/<str:page>/', add_comment, name='add_comment'),
    path('reserve/', views.restaurant_reserve, name='restaurant_reserve'),
    path('thank-you/', views.restaurant_thank_you, name='restaurant_thank_you'),

]