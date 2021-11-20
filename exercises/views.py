from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Breathwork

# Create your views here.

def all_exercises(request):
    """ A view to show all exercises """

    exercises = Breathwork.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('exercises'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            exercises = exercises.filter(queries)

    context = {
        'exercises': exercises,
        'search_term': query,
    }

    return render(request, 'exercises/exercises.html', context)


def breathwork_exercise(request, exercise_id):
    """ A view to show breathwork exercise details """

    exercise = get_object_or_404(Breathwork, pk=exercise_id)

    context = {
        'exercise': exercise,
    }

    return render(request, 'exercises/breathwork_exercise.html', context)