from django.contrib import admin
from .models import Element


class ElementAdmin(admin.ModelAdmin):
    """
    Element admin
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Element, ElementAdmin)
