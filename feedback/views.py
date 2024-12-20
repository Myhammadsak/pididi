from django.db.models import Q
from django.shortcuts import render, redirect

from .forms import FeedbackForm
from .models import Feedback

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = FeedbackForm()

    return render(request, 'feedback/feedback.html', {'form': form})

def feedback_info(request):
    query = request.GET.get('query', '')
    feedback = Feedback.objects.all()

    if query:
        feedback = feedback.filter(Q(user__icontains=query) | Q(message__icontains=query))

    return render(request, 'feedback/feed.html', {'feedback': feedback,
                                                                        'query': query})