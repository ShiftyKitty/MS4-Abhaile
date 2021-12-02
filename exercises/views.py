from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Breathwork, Element

# Create your views here.

def all_exercises(request):
    """ A view to show all exercises """

    exercises = Breathwork.objects.all()
    elements = None
    sort = None
    direction = None

    if 'element' in request.GET:
            elements = request.GET['element'].split(',')
            exercises = exercises.filter(element__name__in=elements)
            elements = Element.objects.filter(name__in=elements)

    context = {
        'exercises': exercises,
        'current_elements': elements,
    }

    return render(request, 'exercises/exercises.html', context)


def breathwork_exercise(request, exercise_id):
    """ A view to show breathwork exercise details """

    exercise = get_object_or_404(Breathwork, pk=exercise_id)

    context = {
        'exercise': exercise,
    }

    return render(request, 'exercises/breathwork_exercise.html', context)