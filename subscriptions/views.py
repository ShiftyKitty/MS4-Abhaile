import json
import stripe
import paypalrestsdk
import logging
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpResponseRedirect
)
from django.conf import settings
from .subscriptions import SubscriptionPlan, set_paid_until

from .models import Subscription


stripe_secret_key = settings.STRIPE_SECRET_KEY # API_KEY 


@require_POST
@login_required
def payment_method(request):
    stripe.api_key = stripe_secret_key
    plan = request.POST.get('plan', 'full')
    context = {}

    plan_inst = SubscriptionPlan(plan_id=plan)
    #               plan_inst.amount
    # 'a' | 'm' =>  plan_inst.currency
    #               plan_inst.stripe_plan_id

    payment_intent = stripe.PaymentIntent.create(
        amount=plan_inst.amount,
        currency=plan_inst.currency,
    )

    context['secret_key'] = payment_intent.client_secret
    context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY
    context['customer_email'] = request.user.email
    context['payment_intent_id'] = payment_intent.id
    context['stripe_plan_id'] = plan_inst.stripe_plan_id

    return render(request, 'subscriptions/subscribe.html', context)

