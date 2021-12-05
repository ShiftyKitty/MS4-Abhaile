# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
# from djstripe.models import Customer, Subscription
# from profiles.models import UserProfile
# from django.conf import settings
# from django.utils.translation import gettext_lazy as _

# class User(AbstractUser):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_subscriber')
#     customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
#     subscription = models.ForeignKey(Subscription, null=True, blank=True,on_delete=models.SET_NULL)