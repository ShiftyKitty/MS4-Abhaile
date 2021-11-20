from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_exercises, name='exercises'),
    path('<exercise_id>', views.breathwork_exercise, name='breathwork_exercise'),
]
