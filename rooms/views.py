from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Room

def room_list(request):
    rooms = Room.objects.filter(is_available=True)
    return render(request, 'rooms/room_list.html', {'rooms': rooms})