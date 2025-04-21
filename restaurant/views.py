from django.shortcuts import render
from .models import RestaurantTable
from comments.models import Comment

def restaurant_list(request):
    tables = RestaurantTable.objects.filter(is_available=True)
    comments = Comment.objects.filter(page='restaurant')
    return render(request, 'restaurant/restaurant_list.html', {'tables': tables, 'comments': comments})

def restaurant_reservation_list(request):
    reservations = RestaurantReservation.objects.all()
    return render(request, 'restaurant/reservation_list.html', {'reservations': reservations})