from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Element

# Create your views here.

def all_elements(request):
    """ A view to show all exercises """

    elements = Element.objects.all()

    context = {
        'elements': elements,
    }

    return render(request, 'elements/elements.html', context)


def element(request, element_id):
    """ A view to show element details """

    element = get_object_or_404(Element, pk=element_id)

    context = {
        'element': element,
    }

    return render(request, 'elements/element.html', context)