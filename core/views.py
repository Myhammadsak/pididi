from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from item.models import Category, Item
from .froms import SignupForm
from django.contrib.auth import logout

from django.utils import timezone
from datetime import timedelta

# Create your views here.
def index(request):
    now = timezone.now()
    week = now - timedelta(days=1)
    recent_products = Item.objects.filter(created_at__gte=week)


    top_items = recent_products.order_by('-purchases')[:6]
    categories = Category.objects.all()
    all_items = Item.objects.order_by('-created_at')[:6]


    return render(request, 'core/index.html', {'top_items': top_items,
                                                                   'categories': categories,
                                                                   'all_items': all_items})

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    item = Item.objects.filter(category=category)

    return render(request, 'core/category_products.html', {'category': category,
                                                                                'items': item})

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/')