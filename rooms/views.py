from django.shortcuts import render
from .models import Room
from comments.models import Comment

def room_list(request):
    rooms = Room.objects.filter(is_available=True)
    comments = Comment.objects.filter(page='rooms')
    return render(request, 'rooms/room_list.html', {'rooms': rooms, 'comments': comments})
