import email
from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import path
from django import forms

# Create your models here.
class CsvImportForm(forms.Form):
    csv_upload=forms.FileField()

class Admin(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
       if not email:
        raise ValueError(_('Please provide an email address'))

       email=self.normalize_email(email) 

       user=self.model(email=email,**extra_fields)

       user.set_password(password)
       user.save()
       return user

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Admin should have is_staff as True'))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Admin should have is_superuser as True'))

        if extra_fields.get('is_active') is not True:
            raise ValueError(_('Admin should have is_active as True'))

        return self.create_user(email,password,**extra_fields)

    # def get_urls(self):
    #     urls=super().get_urls()
    #     new_urls=[path('upload-csv/',self.upload_csv),]
    #     return new_urls+urls

    # def upload_csv(self,request):
    #     form = CsvImportForm()
    #     data
    #     return f'<File Upload >'

class User(AbstractUser):
        username = models.CharField(max_length=25,unique=True)
        email=models.EmailField(max_length=80,unique=True)
        phone_number=PhoneNumberField(null=False,unique=True)

        USERNAME_FIELD='email'

        REQUIRED_FIELDS=['username','phone_number']

        objects=Admin

        def __str__(self):
            return f"<User {self.email}>"