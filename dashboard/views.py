from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator

from item.models import Item, Category
from django.contrib.auth.models import User
from .forms import UserForm, EditItemForm, NewItemForm

@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', context={'items': items})


@login_required
def edit(request):
    user = request.user
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/')
    else:
        form = UserForm(instance=user)

    return render(request, 'dashboard/edit.html', {'user': user, 'form': form})

@login_required
def new_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('/dashboard/')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'dashboard/new_password.html', {'form': form})