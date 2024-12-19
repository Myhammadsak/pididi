from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, \
    PasswordResetConfirmView
from django.urls import path, reverse_lazy
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

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='core/password_reset_form.html',
                                                                 email_template_name='core/password_reset_email.html',
                                                                 success_url=reverse_lazy('core:password_reset_done')),
                                                                    name='password_reset'),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='core/password_reset_done.html'),
                                                    name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='core/password_reset_confirm.html',
                                                    success_url=reverse_lazy('core:password_reset_complete')),
                                                    name='password_reset_confirm'),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='core/password_reset_complete.html'),
                                                        name='password_reset_complete'),
]