from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display=['product_name','price','ordered_quantity','created_at']
    list_filter=['product_name','price','created_at']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['customer','amount','status']
    list_filter=['customer','item','amount','datetimestamp','status']

@admin.register(OrderDetails)
class OrderDetailsAdmin(admin.ModelAdmin):
    list_display=['order','product','quantity']
    list_filter=['order','product','quantity']

