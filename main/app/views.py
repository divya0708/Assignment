from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from . import serializers
from .models import *
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class HelloAppView(generics.GenericAPIView):
    def get(self,request):
        return Response(data={'message':'Hello Apps'},status=status.HTTP_200_OK)


class ItemListView(generics.GenericAPIView):
    serializer_class=serializers.ItemCreationSerializer
    queryset=Item.objects.all()
    permission_classes=[IsAuthenticated]
    
    def get(self,request):
        items = Item.objects.all()

        serializer=self.serializer_class(instance=items,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        data=request.data

        serializer=self.serializer_class(data=data)

        user=request.user

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
# class OrderListView()

class OrderDetailsView(generics.GenericAPIView):

    def get(self,request,order):
        pass

    def put(self,request,order):
        pass

    def delete(self,request,order):
        pass
