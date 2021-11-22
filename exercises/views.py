from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Breathwork

# Create your views here.

def all_exercises(request):
    """ A view to show all exercises """

    exercises = Breathwork.objects.all()

    context = {
        'exercises': exercises,
    }

    return render(request, 'exercises/exercises.html', context)


def breathwork_exercise(request, exercise_id):
    """ A view to show breathwork exercise details """

    exercise = get_object_or_404(Breathwork, pk=exercise_id)

    context = {
        'exercise': exercise,
    }

    return render(request, 'exercises/breathwork_exercise.html', context)