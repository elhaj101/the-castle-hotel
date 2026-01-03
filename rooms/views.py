from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone

from comments.models import Comment
from .forms import ReservationForm
from .models import Room, Reservation

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
        'today': today,
    })


@login_required
def reservation_list(request):
    reservations = (
        Reservation.objects.filter(guest=request.user)
        .select_related('room')
        .order_by('-check_in_date')
    )
    return render(request, 'rooms/reservations.html', {'reservations': reservations})


@login_required
def room_details(request):
    if request.method == 'POST':
        room_type = request.POST.get('room_type')
        room = Room.objects.filter(room_type=room_type, is_available=True).first()
        form = ReservationForm(request.POST)

        if not room:
            form.add_error(None, 'No available rooms of this type.')

        if form.is_valid() and room:
            reservation = form.save(commit=False)
            reservation.guest = request.user
            reservation.room = room
            nights = (reservation.check_out_date - reservation.check_in_date).days
            reservation.total_price = Decimal(nights) * room.price_per_night
            reservation.save()
            room.is_available = False
            room.save()
            messages.success(request, 'Reservation created.')
            return redirect('reservation_list')

        return render(request, 'rooms/interactive/details.html', {
            'room_type': room_type,
            'check_in_date': request.POST.get('check_in_date', ''),
            'check_out_date': request.POST.get('check_out_date', ''),
            'available_room_type': room.room_type if room else None,
            'form': form,
        })

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
        'form': ReservationForm(initial={
            'check_in_date': check_in_date or None,
            'check_out_date': check_out_date or None,
        }),
    })


@login_required
def reservation_edit(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id, guest=request.user)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            reservation = form.save(commit=False)
            nights = (reservation.check_out_date - reservation.check_in_date).days
            reservation.total_price = Decimal(nights) * reservation.room.price_per_night
            reservation.save()
            messages.success(request, 'Reservation updated.')
            return redirect('reservation_list')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'rooms/reservation_edit.html', {
        'reservation': reservation,
        'form': form,
    })


@login_required
def reservation_delete(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id, guest=request.user)
    if request.method == 'POST':
        room = reservation.room
        reservation.delete()
        room.is_available = True
        room.save()
        messages.success(request, 'Reservation deleted.')
        return redirect('reservation_list')
    return render(request, 'rooms/reservation_confirm_delete.html', {'reservation': reservation})
