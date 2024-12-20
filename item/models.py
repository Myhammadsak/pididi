from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Item(models.Model):

    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    purchases = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class PurchaseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    price = models.FloatField()
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'History: {self.name} - {self.price}'