from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from item.models import Category, Item
from .models import Cart
from .froms import SignupForm
from django.contrib.auth import logout

from django.utils import timezone
from datetime import timedelta



def index(request):
    now = timezone.now()
    week = now - timedelta(days=7)
    recent_products = Item.objects.filter(created_at__gte=week)


    top_items = recent_products.order_by('-purchases')[:6]
    categories = Category.objects.all()
    all_items = Item.objects.order_by('-created_at')[:6]


    return render(request, 'core/index.html', {'top_items': top_items,
                                                                   'categories': categories,
                                                                   'all_items': all_items})

def category_products(request, pk):
    category = get_object_or_404(Category, pk=pk)
    item = Item.objects.filter(category=category)

    return render(request, 'core/category_products.html', {'category': category,
                                                                                'items': item})

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


@login_required
def add_cart(request, pk):
    product = get_object_or_404(Item, pk=pk)
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('/')

@login_required
def remove_cart(request, pk):
    product = get_object_or_404(Item, pk=pk)
    Cart.objects.filter(user=request.user, product=product).delete()
    return redirect('/cart')

@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'core/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

@login_required
def update_cart(request, pk, action):
    product = get_object_or_404(Item, id=pk)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

    if action == 'add':
        cart_item.quantity += 1
    elif action == 'remove':
        if cart_item.quantity > 1:
            cart_item.quantity -= 1

    cart_item.save()
    return redirect(f'/cart/{pk}/')

def cart_detail(request, pk):
    product = get_object_or_404(Item, pk=pk)
    cart_items = Cart.objects.filter(user=request.user, product=product)
    total_item_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'core/cart_detail.html', {'cart_items': cart_items,
                                                                        'total_item_price': total_item_price})