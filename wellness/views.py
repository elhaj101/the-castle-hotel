from django.shortcuts import render
from .models import Treatment, Appointment
from comments.models import Comment

def wellness_list(request):
    comments = Comment.objects.filter(page='wellness')
    return render(request, 'wellness/wellness_list.html', {'comments': comments})


def treatment_list(request):
    treatments = Treatment.objects.all()
    return render(request, 'wellness/treatment_list.html', {'treatments': treatments})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'wellness/appointment_list.html', {'appointments': appointments})