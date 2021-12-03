from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_exercises, name='exercises'),
    path('<int:exercise_id>/', views.breathwork_exercise, name='breathwork_exercise'),
    path('add/', views.add_breathwork_exercise, name='add_breathwork_exercise'),
    path('edit/<int:exercise_id>/', views.edit_breathwork_exercise, name='edit_breathwork_exercise'),
    path('delete/<int:exercise_id>/', views.delete_exercise, name='delete_exercise'),
]
