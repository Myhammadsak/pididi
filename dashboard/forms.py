from django import forms
from django.contrib.auth.models import User
from item.models import Item

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))