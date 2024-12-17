from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import NewItemForm, EditItemForm
from .models import Item, Category, PurchaseHistory


def create_purchase_history(user, product, quantity=1):
    PurchaseHistory.objects.create(
        user=user,
        image=product.image,
        name=product.name,
        price=product.price,
        quantity=quantity
    )


def item(request):
    query = request.GET.get('query', '')
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    category_id = request.GET.get('category', 0)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    paginator = Paginator(items, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'item/items.html', context={'items': items,
                                                       'query': query,
                                                       'categories': categories,
                                                       'category_id': int(category_id),
                                                       'page_obj': page_obj})

def detail(request, pk):

    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', context={'item': item, 'related_items': related_items})

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)

    else:
        form = NewItemForm()

    form = NewItemForm()
    return render(request, 'item/form.html', context={'form': form, 'title': 'New item'})

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)

    else:
        form = EditItemForm(instance=item)

    form = EditItemForm()
    return render(request, 'item/form.html', context={'form': form, 'title': 'Edit item'})

@login_required
def buy(request, pk):
    user = request.user
    product = Item.objects.get(pk=pk)
    quantity = int(request.POST.get('quantity', 1))
    create_purchase_history(user, product, quantity)

    item = get_object_or_404(Item, pk=pk)
    item.purchases += 1
    item.save()

    return render(request, 'item/detail.html', {'item': item})

@login_required
def history(request):
    history = PurchaseHistory.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'item/history.html', {'history': history})