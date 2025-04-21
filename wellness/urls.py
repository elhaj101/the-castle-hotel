from django.urls import path
from . import views
from comments.views import add_comment

urlpatterns = [
    path('', views.wellness_list, name='wellness_list'),
    path('comment/add/<str:page>/', add_comment, name='add_comment'),
    path('treatments/', views.treatment_list, name='treatment_list'),
    path('appointments/', views.appointment_list, name='appointment_list'),
]


