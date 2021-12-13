from django.contrib import admin
from .models import Breathwork


class BreathworkAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'element',
        'image',
        'youtube_link'
    )

    ordering = ('name',)


admin.site.register(Breathwork, BreathworkAdmin)
