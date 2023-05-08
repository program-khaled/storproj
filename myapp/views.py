from django.shortcuts import render
from .models import clothes,shoe,accessory,bag,global_brand,sunglas,wristwatch
from django.contrib.auth.decorators import login_required
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.decorators import user_passes_test

def dash_view(request):
    obj_global_brand = global_brand.objects.all()
    user_has_access = request.user.username == 'abood' and request.user.check_password('1234')
    return render(request,'index.html',{'obj_global_brand':obj_global_brand,'user_has_access': user_has_access})

def clothes_view(request):
    obj_clothes = clothes.objects.all()
    user_has_access = request.user.username == 'abood' and request.user.check_password('1234')
    return render(request, 'clothes.html',{'obj_clothes':obj_clothes,'user_has_access': user_has_access})

def shoe_view(request):
    obj_shoe = shoe.objects.all()
    user_has_access = request.user.username == 'abood' and request.user.check_password('1234')
    return render(request, 'shoe.html',{'obj_shoe':obj_shoe,'user_has_access': user_has_access})




def wristwatch_view(request):
    obj_wristwatch = wristwatch.objects.all()
    user_has_access = request.user.username == 'abood' and request.user.check_password('1234')

    return render(request, 'wristwatch.html',{'obj_wristwatch':obj_wristwatch,'user_has_access': user_has_access})

def bag_view(request):
    obj_bag = bag.objects.all()
    user_has_access = request.user.username == 'abood' and request.user.check_password('1234')

    return render(request, 'bag.html',{'obj_bag':obj_bag,'user_has_access': user_has_access})
def sunglas_view(request):
    obj_sunglas = sunglas.objects.all()
    user_has_access = request.user.username == 'abood' and request.user.check_password('1234')
    return render(request, 'sunglas.html',{'obj_sunglas':obj_sunglas,'user_has_access': user_has_access})
def accessory_view(request):
    obj_accessory = accessory.objects.all()
    user_has_access = request.user.username == 'abood' and request.user.check_password('1234')

    return render(request, 'accessory.html',{'obj_accessory':obj_accessory,'user_has_access': user_has_access})

def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("login")
    return render(request, "registration/signup.html", {"form": form})





def add_bag_view(request):
    if request.method == 'POST':
        form = add_bag_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dash_view')
    else:
        form = add_bag_form()

    return render(request, 'add_bag.html', {'form': form})
    
def add_accessory_view(request):
    if request.method == 'POST':
        form = add_accessory_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dash_view')
    else:
        form = add_accessory_form()

    return render(request, 'add_accessory.html', {'form': form})

def add_clothes_view(request):
    if request.method == 'POST':
        form = add_clothes_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dash_view')
    else:
        form = add_clothes_form()

    return render(request, 'add_clothes.html', {'form': form})

def add_shoe_view(request):
    if request.method == 'POST':
        form = add_shoe_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dash_view')
    else:
        form = add_shoe_form()

    return render(request, 'add_shoe.html', {'form': form})

def add_sunglas_view(request):
    if request.method == 'POST':
        form = add_sunglas_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dash_view')
    else:
        form = add_sunglas_form()

    return render(request, 'add_sunglas.html', {'form': form})

def add_wristwatch_view(request):
    if request.method == 'POST':
        form = add_wristwatch_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dash_view')
    else:
        form = add_wristwatch_form()

    return render(request, 'add_wristwatch.html', {'form': form})

def add_global_brand_view(request):
    if request.method == 'POST':
        form = add_global_brand_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dash_view')
    else:
        form = add_global_brand_form()

    return render(request, 'add_global_brand.html', {'form': form})
