from django import forms
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=255, required=True, widget=forms.EmailInput())
    phonnumber = forms.CharField(max_length=20,required=False)
    class Meta:
        model=User
        fields = ["username", "email", "password1", "password2",'phonnumber']

class add_bag_form(forms.ModelForm):
    
    class Meta:
        model=bag
        fields = ["name", "price", "desc", "image"]

class add_accessory_form(forms.ModelForm):
    
    class Meta:
        model=accessory
        fields = ["name", "price", "desc", "image"]

class add_clothes_form(forms.ModelForm):
    
    class Meta:
        model=clothes
        fields = ["name", "price", "desc", "image"]

class add_shoe_form(forms.ModelForm):
    
    class Meta:
        model=shoe
        fields = ["name", "price", "desc", "image"]

class add_sunglas_form(forms.ModelForm):
    
    class Meta:
        model=sunglas
        fields = ["name", "price", "desc", "image"]

class add_wristwatch_form(forms.ModelForm):
    
    class Meta:
        model=wristwatch
        fields = ["name", "price", "desc", "image"]

class add_global_brand_form(forms.ModelForm):
    
    class Meta:
        model=global_brand
        fields = ["name","brand_name", "price", "desc", "image"]

