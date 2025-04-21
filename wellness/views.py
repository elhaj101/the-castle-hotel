from django.shortcuts import render, redirect
from .models import Treatment, Appointment
from comments.models import Comment
from django.contrib.auth.decorators import login_required
import datetime

def wellness_list(request):
    treatments = Treatment.objects.all()
    comments = Comment.objects.filter(page='wellness')
    today = datetime.date.today().isoformat()
    return render(request, 'wellness/wellness_list.html', {
        'treatments': treatments,
        'comments': comments,
        'today': today
    })

@login_required
def book_appointment(request):
    if request.method == 'POST':
        reservation_name = request.POST.get('reservation_name')
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        # Remove treatment logic
        exists = Appointment.objects.filter(
            appointment_date=appointment_date,
            appointment_time=appointment_time
        ).exists()
        if not exists:
            Appointment.objects.create(
                guest=request.user,
                reservation_name=reservation_name,
                appointment_date=appointment_date,
                appointment_time=appointment_time
            )
            return redirect('wellness_thank_you')
        else:
            return redirect('wellness_list')
    return redirect('wellness_list')

def wellness_thank_you(request):
    return render(request, 'wellness/interactive/thank_you.html')