from django.contrib.admin import AdminSite
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from core.models import Cart
from feedback.models import Feedback
from item.models import Item, Category, PurchaseHistory


class CustomAdminSite(AdminSite):
    site_header = "Моя кастомная админка"
    site_title = "Управление сайтом"
    index_title = "Добро пожаловать в панель управления"

# Инициализация кастомной админки
custom_admin_site = CustomAdminSite(name="custom_admin")

# Регистрация моделей с использованием стандартного функционала ModelAdmin
custom_admin_site.register(User, admin.ModelAdmin)
custom_admin_site.register(Cart, admin.ModelAdmin)
custom_admin_site.register(Feedback, admin.ModelAdmin)
custom_admin_site.register(Item, admin.ModelAdmin)
custom_admin_site.register(Category, admin.ModelAdmin)
custom_admin_site.register(PurchaseHistory, admin.ModelAdmin)


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'stock')
#     search_fields = ('name',)


