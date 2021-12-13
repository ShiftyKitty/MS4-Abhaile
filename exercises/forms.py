from django import forms
from elements.models import Element
from .widgets import CustomClearableFileInput
from .models import Breathwork


class BreathworkForm(forms.ModelForm):
    """
    Form for Breathwork
    """

    class Meta:
        """
        Meta class
        """
        model = Breathwork
        fields = '__all__'

    image = forms.ImageField(
        label='Image (required)',
        required=True, widget=CustomClearableFileInput)
    youtube_link = forms.URLField(
        label='Youtube Embed Link (required)', required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        elements = Element.objects.all()
        friendly_names_e = [(e.id, e.get_friendly_name()) for e in elements]

        self.fields['element'].choices = friendly_names_e
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
