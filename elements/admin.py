from django.contrib import admin
from .models import Element

# Register your models here.
class ElementAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Element, ElementAdmin)
