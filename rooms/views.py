from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Room, Reservation
from comments.models import Comment
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

def room_list(request):
    double_room = Room.objects.filter(room_type="Double Room").first()
    single_room = Room.objects.filter(room_type="Single Room").first()
    suite = Room.objects.filter(room_type="Suite").first()
    comments = Comment.objects.filter(page='rooms')
    today = timezone.now().date().isoformat()  # Add this line
    return render(request, 'rooms/room_list.html', {
        'double_room': double_room,
        'single_room': single_room,
        'suite': suite,
        'comments': comments,
        'today': today,  # Add this line
    })

@login_required
def room_details(request):
    if request.method == 'POST':
        # Get all form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        nationality = request.POST.get('nationality')
        children = request.POST.get('children')
        extras = request.POST.getlist('extras')
        agree = request.POST.get('agree')
        room_type = request.POST.get('room_type')
        check_in_date = request.POST.get('check_in_date')
        check_out_date = request.POST.get('check_out_date')

        # Find an available room of the selected type
        room = Room.objects.filter(room_type=room_type, is_available=True).first()
        if not room:
            return render(request, 'rooms/interactive/details.html', {
                'room_type': room_type,
                'check_in_date': check_in_date,
                'check_out_date': check_out_date,
                'error': 'No available rooms of this type.'
            })

        # Calculate total price
        nights = (datetime.datetime.strptime(check_out_date, "%Y-%m-%d") - datetime.datetime.strptime(check_in_date, "%Y-%m-%d")).days
        total_price = nights * float(room.price_per_night)

        # Save reservation (add extra fields as needed)
        Reservation.objects.create(
            guest=request.user,
            room=room,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            total_price=total_price,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            nationality=nationality,
            children=children,
            extras=",".join(extras),  # or use a ManyToManyField if you want
            agree=bool(agree),
        )
        room.is_available = False
        room.save()
        return redirect('room_list')

    # For GET, pass booking info to the template and show available room type
    room_type = request.GET.get('room_type', '')
    check_in_date = request.GET.get('check_in_date', '')
    check_out_date = request.GET.get('check_out_date', '')
    room = Room.objects.filter(room_type=room_type, is_available=True).first()
    available_room_type = room.room_type if room else None
    return render(request, 'rooms/interactive/details.html', {
        'room_type': room_type,
        'check_in_date': check_in_date,
        'check_out_date': check_out_date,
        'available_room_type': available_room_type,
    })



def your_view(request):
    today = timezone.now().date().isoformat()
    # ...other context...
    return render(request, 'your_template.html', {'today': today})