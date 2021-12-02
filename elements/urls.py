from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_elements, name='elements'),
    path('<element_id>', views.element, name='element'),
]
