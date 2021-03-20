from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.

"""
An inline allows you to include a model on the same edit page
as its related model. Used ModelInline class for the OrderItem
model to include is as an inline in the OrderAdmin class
"""


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
