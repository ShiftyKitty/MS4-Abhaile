from django.shortcuts import render
from elements.models import Element
from elements.views import element

# Create your views here.

def index(request):
    """ A view to return the index page """

    elements = Element.objects.all()

    context = {
        'elements': elements,
    }

    return render(request, 'home/index.html', context)