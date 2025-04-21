from django.shortcuts import render, redirect
from .models import RestaurantTable, RestaurantReservation
from comments.models import Comment
from django.contrib.auth.decorators import login_required



def restaurant_list(request):
    tables = RestaurantTable.objects.all()
    comments = Comment.objects.filter(page='restaurant')
    return render(request, 'restaurant/restaurant_list.html', {'tables': tables, 'comments': comments})

def restaurant_reservation_list(request):
    reservations = RestaurantReservation.objects.all()
    return render(request, 'restaurant/reservation_list.html', {'reservations': reservations})

@login_required
def restaurant_reserve(request):
    if request.method == 'POST':
        reservation_name = request.POST.get('reservation_name')
        reservation_date = request.POST.get('reservation_date')
        reservation_time = request.POST.get('reservation_time')
        reserved_tables = RestaurantReservation.objects.filter(
            reservation_date=reservation_date,
            reservation_time=reservation_time
        ).values_list('table_id', flat=True)
        table = RestaurantTable.objects.exclude(id__in=reserved_tables).first()
        if table:
            RestaurantReservation.objects.create(
                guest=request.user,
                table=table,
                reservation_name=reservation_name,
                reservation_date=reservation_date,
                reservation_time=reservation_time
            )
            return redirect('restaurant_thank_you')  # Success: go to thank you page
        else:
            # No tables available for this slot
            return redirect('restaurant_list')  # Or show a "no tables" message
    return redirect('restaurant_list')

def restaurant_thank_you(request):
    return render(request, 'restaurant/interactive/restaurant_thank_you.html')