from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['user', 'email', 'message']

    user = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your name',
        'class': 'mb-4 w-full py-4 px-6 rounded-xl'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email',
        'class': 'mb-4 w-full py-4 px-6 rounded-xl'
    }))

    message = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Message',
        'class': 'mb-4 w-full py-4 px-6 rounded-xl'
    }))