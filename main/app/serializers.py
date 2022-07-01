from dataclasses import field
from .models import *
from rest_framework import serializers


class ItemCreationSerializer(serializers.ModelSerializer):
    product_name=serializers.CharField(max_length=255)
    price=serializers.DecimalField(max_digits=15,decimal_places=2)
    ordered_quantity=serializers.IntegerField()

    class Meta:
        model=Item
        fields=['product_name','price','ordered_quantity']


class OrderCreationSerializer(serializers.ModelSerializer):
    amount = serializers.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1000000)])
    status = serializers.CharField(max_length=10)

    class Meta:
        model=Item
        fields=['amount','status']


class OrderDetailsCreationSerializer(serializers.ModelSerializer):
    quantity = models.PositiveIntegerField()

    class Meta:
        model=Item
        fields=['quantity']


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()


class SaveFileSerializer(serializers.Serializer):
    
    class Meta:
        model = Item
        fields = "__all__"