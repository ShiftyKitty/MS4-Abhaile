from django.contrib import admin
from .models import Subscriber, Subscription


class AdminSubscription(admin.ModelAdmin):
    pass


class AdminSubscriber(admin.ModelAdmin):
    pass


admin.site.register(Subscription, AdminSubscription)
admin.site.register(Subscriber, AdminSubscriber)