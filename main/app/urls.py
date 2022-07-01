from unicodedata import name
from django.urls import path
from .import views

urlpatterns=[
    path('',views.HelloAppView.as_view(),name='hello_app'),
    path('items/',views.ItemListView.as_view(), name='items')
]