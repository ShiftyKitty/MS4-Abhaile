# import logging
# import stripe
# from .models import User

# from django.conf import settings

# FIRE = 'f'
# WATER = 'w'
# AIR = 'a'
# EARTH = 'er'
# FULL = 'full'

# API_KEY = settings.STRIPE_SECRET_KEY
# logger = logging.getLogger(__name__)


# class FireSubPlan:
#     def __init__(self):
#         self.stripe_plan_id = settings.FIRE_SUBSCRIPTION
#         self.amount = 495

# class WaterSubPlan:
#     def __init__(self):
#         self.stripe_plan_id = settings.WATER_SUBSCRIPTION
#         self.amount = 495

# class AirSubPlan:
#     def __init__(self):
#         self.stripe_plan_id = settings.AIR_SUBSCRIPTION
#         self.amount = 495

# class EarthSubPlan:
#     def __init__(self):
#         self.stripe_plan_id = settings.EARTH_SUBSCRIPTION
#         self.amount = 495

# class FullSubPlan:
#     def __init__(self):
#         self.stripe_plan_id = settings.FULL_SUBSCRIPTION
#         self.amount = 1000


# class SubscriptionPlan:
#     def __init__(self, plan_id):
#         """
#         plan_id is either string 'f' (stands for fire),
#         string letter 'w' (which stands for water),
#         string letter 'a' (which stands for air),
#         string letter 'er' (which stands for earth),
#         string 'full' (which stands for full),
#         """
#         if plan_id == FIRE:
#             self.plan = FireSubPlan()
#             self.id = FIRE
#         elif plan_id == WATER:
#             self.plan = WaterSubPlan()
#             self.id = WATER
#         elif plan_id == AIR:
#             self.plan = AirSubPlan()
#             self.id = AIR
#         elif plan_id == EARTH:
#             self.plan = EarthSubPlan()
#             self.id = EARTH
#         elif plan_id == FULL:
#             self.plan = FullSubPlan()
#             self.id = FULL
#         else:
#             raise ValueError('Invalid plan_id value')

#         self.currency = 'eur'

#     @property
#     def stripe_plan_id(self):
#         return self.plan.stripe_plan_id

#     @property
#     def amount(self):
#         return self.plan.amount


# def set_paid_until(charge):
#     logger.info(f"set_paid_until with {charge}")

#     stripe.api_key = API_KEY
#     pi = stripe.PaymentIntent.retrieve(charge.payment_intent)

#     if pi.customer:
#         customer = stripe.Customer.retrieve(pi.customer)
#         email = customer.email

#         if customer:
#             subscr = stripe.Subscription.retrieve(
#                 customer['subscriptions'].data[0].id
#             )
#             current_period_end = subscr['current_period_end']

#         try:
#             subscriber = Subscriber.objects.get(email=email)
#         except Subscriber.DoesNotExist:
#             logger.warning(
#                 f"Subscriber with email {email} not found"
#             )
#             return False

#         subscriber.set_paid_until(current_period_end)
#         logger.info(
#             f"Profile with {current_period_end} saved for subscriber {email}"
#         )
#     else:
#         pass
#         # charge.amount  1990 | 19995
#         # this was one time payment, update
#         # paid_until (e.g. paid_until = current_date + 31 days) using
#         # charge.paid + charge.amount attrs