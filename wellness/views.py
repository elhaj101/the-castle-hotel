from django.shortcuts import render
from .models import WellnessSession
from comments.models import Comment

def wellness_list(request):
    sessions = WellnessSession.objects.filter(is_available=True)
    comments = Comment.objects.filter(page='wellness')
    return render(request, 'wellness/wellness_list.html', {'sessions': sessions, 'comments': comments})
