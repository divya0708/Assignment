from unicodedata import name
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


# Create your models here.

User=get_user_model()

# class Category(models.Model):
#     name=models.CharField(max_length=255)

#     @staticmethod
#     def get_all_categories():
#         return Category.objects.all()

#     def __str__(self):
#         return self.name

class Item(models.Model):
    product_name=models.CharField(max_length=255, blank=False)
    price=models.DecimalField(max_digits=15,decimal_places=2,default=0.00)
    ordered_quantity=models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    # file=models.FileField(blank = True, editable = True, upload_to='C://Coding_assignment//main//main//static_files')

    def __str__(self):
        return f"<Item {self.product_name}><Price {self.price}><Quantity {self.ordered_quantity}>"

class Order(models.Model):
    STATUS = [
        ('success', _('SUCCESS')),
        ('pending', _('PENDING')),
        ('failed', _('FAILED')),
    ]
    customer=models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    item=models.ManyToManyField(Item,related_name='ordered_item',default=[0])
    amount = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1000000)],default=0)
    datetimestamp = models.DateTimeField(default=datetime.now(),blank=True)
    status = models.CharField(max_length=10, choices=STATUS,default='success')

    def __str__(self):
        return f"<Customer {self.customer.id}> <Item {self.item}> <Amount {self.amount}> <Order_Status {self.status}>"

class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_details')
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"<Order {self.order.id}>< Product {self.product.id}>< Quantity {self.quantity}>"



