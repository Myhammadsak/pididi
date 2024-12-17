from django.shortcuts import render, redirect

from .forms import FeedbackForm

# Create your views here.
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = FeedbackForm()

    return render(request, 'feedback/feedback.html', {'form': form})