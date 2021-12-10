from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category
from elements.models import Element


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image_1 = forms.ImageField(label='Image 1 (required)', required=True, widget=CustomClearableFileInput)
    image_2 = forms.ImageField(label='Image 2', required=False, widget=CustomClearableFileInput)
    image_3 = forms.ImageField(label='Image 3', required=False, widget=CustomClearableFileInput)
    image_4 = forms.ImageField(label='Image 4', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        elements = Element.objects.all()
        friendly_names_c = [(c.id, c.get_friendly_name()) for c in categories]
        friendly_names_e = [(e.id, e.get_friendly_name()) for e in elements]

        self.fields['category'].choices = friendly_names_c
        self.fields['element'].choices = friendly_names_e
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'