from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_subscriptions, name='all_subscriptions'),
    path('subscribe_checkout/', views.subscribe_checkout, name='subscribe_checkout'),
    path('subscribe_success/', views.subscribe_success, name='subscribe_success'),
    path('payment-method', views.payment_method, name='payment_method'),
]