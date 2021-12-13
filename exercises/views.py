from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Breathwork, Element
from .forms import BreathworkForm


# Create your views here.

def all_exercises(request):
    """ A view to show all exercises """

    exercises = Breathwork.objects.all()
    elements = None

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


@login_required
def add_breathwork_exercise(request):
    """ Add a breathwork_exercise to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BreathworkForm(request.POST, request.FILES)
        if form.is_valid():
            exercise = form.save()
            messages.success(request, 'Successfully added exercise!')
            return redirect(reverse('breathwork_exercise', args=[exercise.id]))
        else:
            messages.error(
                request,
                'Failed to add exercise. Please ensure the form is valid.')
    else:
        form = BreathworkForm()

    template = 'exercises/add_breathwork_exercise.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_breathwork_exercise(request, exercise_id):
    """ Edit a breathwork exercise in the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse('home'))

    exercise = get_object_or_404(Breathwork, pk=exercise_id)
    if request.method == 'POST':
        form = BreathworkForm(request.POST, request.FILES, instance=exercise)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated exercise!')
            return redirect(reverse('breathwork_exercise', args=[exercise.id]))
        else:
            messages.error(
                request,
                'Failed to update exercise. Please ensure the form is valid.')
    else:
        form = BreathworkForm(instance=exercise)
        messages.info(request, f'You are editing {exercise.name}')

    template = 'exercises/edit_breathwork_exercise.html'
    context = {
        'form': form,
        'exercise': exercise,
    }

    return render(request, template, context)


@login_required
def delete_exercise(request, exercise_id):
    """ Delete a exercise from the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse('home'))

    exercise = get_object_or_404(Breathwork, pk=exercise_id)
    exercise.delete()
    messages.success(request, 'Exercise deleted!')
    return redirect(reverse('exercises'))
