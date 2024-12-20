from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ChatMessage

@login_required
def chat_room(request, room_name=None):
    if request.user.is_superuser and room_name:
        return render(request, 'adminchat/chat_room.html', {'room_name': room_name})

    room_name = f'user_{request.user.username}'
    return render(request, 'adminchat/chat_room.html', {'room_name': room_name})

@login_required
def chat_list(request):
    if not request.user.is_superuser:
        return render(request, 'adminchat/error.html', {'error': 'Доступ запрещен'})

    rooms = ChatMessage.objects.values('room_name').distinct()
    return render(request, 'adminchat/chat_list.html', {'rooms': rooms})
