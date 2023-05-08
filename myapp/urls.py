from django.urls import path
from myapp.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',dash_view,name='dash_view'),
    path('shoes/',shoe_view,name='shoe_view'),
    path('clothes/',clothes_view,name='clothes_view'),
    path('accessory/',accessory_view,name='accessory_view'),
    path('bag/',bag_view,name='bag_view'),
    path('sunglas/',sunglas_view,name='sunglas_view'),
    path('wristwatch/',wristwatch_view,name='wristwatch_view'),


     # ... other URL patterns ...
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
     path("signup/", signup, name="signup"),

   
    path('add_bag/', add_bag_view,name='add_bag_view'),
    path('add_accessory/', add_accessory_view,name='add_accessory_view'),

    path('add_clothes/', add_clothes_view,name='add_clothes_view'),
    path('add_shoe/', add_shoe_view,name='add_shoe_view'),

    path('add_sunglas/', add_sunglas_view,name='add_sunglas_view'),
    path('add_wristwatch/', add_wristwatch_view,name='add_wristwatch_view'),
    path('add_global_brand/', add_global_brand_view,name='add_global_brand_view'),



]