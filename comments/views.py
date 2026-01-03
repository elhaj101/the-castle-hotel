from django.shortcuts import redirect
from .models import Comment
from django.contrib.auth.decorators import login_required

@login_required
def add_comment(request, page):
    if request.method == 'POST':
        text = request.POST.get('text')
        Comment.objects.create(user=request.user, text=text, page=page)
        return redirect(request.META.get('HTTP_REFERER', 'home'))  # Redirect back to the page
    return redirect('home')
