from django.urls import path
from . import views
from comments.views import add_comment

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('comment/add/<str:page>/', add_comment, name='add_comment'),
    # path('reservations/', views.book_room, name='book_room'),  # POST handler for modal
    path('details/', views.room_details, name='room_details'),
]