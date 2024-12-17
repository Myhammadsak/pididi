from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .froms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),

    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm),
         name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('category/<int:pk>/', views.category_products, name='category_products'),

    path('cart_add/<int:pk>/', views.add_cart, name='add_cart'),
    path('cart_remove/<int:pk>/', views.remove_cart, name='remove_cart'),
    path('cart/', views.cart, name='cart'),
    path('update/<int:pk>/<str:action>/', views.update_cart, name='update_cart'),
    path('cart/<int:pk>/', views.cart_detail, name='cart_detail'),
    path('allcartbuy/', views.all_cart_buy, name='all_cart_buy'),

    # path('feedback/', views.feedback, name='feedback')
]