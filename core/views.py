from django.shortcuts import render, redirect, get_object_or_404
from item.models import Category, Item
from .froms import SignupForm
from django.contrib.auth import logout

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    context = {
        'items': items,
        'categories': categories
    }

    return render(request, 'core/index.html', context=context)

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
    return render(request, 'core/signup.html', context={'form': form})

def logout_view(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/')