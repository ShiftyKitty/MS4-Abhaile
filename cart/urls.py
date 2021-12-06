from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('subscribe/<sub_id>/', views.add_element_to_cart, name='add_element_to_cart'),
    path('remove_subscribe/<sub_id>/', views.remove_element_from_cart, name='remove_element_from_cart'),
    path('adjust/<item_id>/', views.adjust_cart, name='adjust_cart'),
    path('remove/<item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
