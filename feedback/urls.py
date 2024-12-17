from django.urls import path
from . import views

app_name = 'feed'

urlpatterns = [
    path('feedback/', views.feedback, name='feedback')
]