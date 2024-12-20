from django.urls import path
from . import views

app_name = 'adminchat'

urlpatterns = [
    path('chat/', views.chat_room, name='chat_room'),
    path('chat/admin/<str:room_name>/', views.chat_room, name='admin_chat_room'),
    path('chat/list/', views.chat_list, name='chat_list'),
]
