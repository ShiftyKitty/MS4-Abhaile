import json
import stripe
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
logger = logging.getLogger(__name__)

@login_required
def all_subscriptions(request):
    logger.info("all_subscriptions")
    return render(request, 'subscriptions/all_subscriptions.html')


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


@login_required
def subscribe_checkout(request):

    payment_intent_id = request.POST['payment_intent_id']
    payment_method_id = request.POST['payment_method_id']
    stripe_plan_id = request.POST['stripe_plan_id']
    stripe.api_key = stripe_secret_key

   
    customer = stripe.Customer.create(
        email=request.user.email,
        payment_method=payment_method_id,
        invoice_settings={
            'default_payment_method': payment_method_id
        }
    )

    s = stripe.Subscription.create(
        customer=customer.id,
        items=[
            {
                'plan': stripe_plan_id
            },
        ]
    )
    latest_invoice = stripe.Invoice.retrieve(s.latest_invoice)

    ret = stripe.PaymentIntent.confirm(
        latest_invoice.payment_intent
    )

    if ret.status == 'requires_action':
        pi = stripe.PaymentIntent.retrieve(
            latest_invoice.payment_intent
        )
        context = {}
        context['payment_intent_secret'] = pi.client_secret
        context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY

        return render(request, 'land/payments/3dsec.html', context)

    return render(request, 'land/payments/thank_you.html')

def subscribe_success(request, order_number):
    """
    Handle successful subscriptions
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)