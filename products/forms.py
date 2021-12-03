from django import forms
from .models import Product, Category
from elements.models import Element


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        elements = Element.objects.all()
        friendly_names_c = [(c.id, c.get_friendly_name()) for c in categories]
        friendly_names_e = [(e.id, e.get_friendly_name()) for e in elements]

        self.fields['category'].choices = friendly_names_c
        self.fields['element'].choices = friendly_names_e
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'