from django.shortcuts import render, get_object_or_404
from exercises.models import Breathwork
from products.models import Product
from .models import Element


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
    products = Product.objects.all()
    exercises = Breathwork.objects.all()

    context = {
        'element': element,
        'products': products,
        'exercises': exercises
    }

    return render(request, 'elements/element.html', context)
