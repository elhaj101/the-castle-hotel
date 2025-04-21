from django.urls import path
from . import views
from comments.views import add_comment

urlpatterns = [
    path('', views.wellness_list, name='wellness_list'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('thank-you/', views.wellness_thank_you, name='wellness_thank_you'),
    path('comment/add/<str:page>/', add_comment, name='add_comment'),
]

