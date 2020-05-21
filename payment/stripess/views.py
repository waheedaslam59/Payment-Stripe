import app as app
from django.shortcuts import render
from django.conf import settings
from django.views.generic.base import TemplateView
import stripe
from .models import *
stripe.api_key = "sk_test_5ZGIp68bSfUGXCwamAsEvlME00mep8Dg4U"


class HomePageView(TemplateView):
    template_name = 'stripess/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def charge(request):
    if request.method == 'POST':
        users = request.user
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        order = Orders()
        order.user = users
        order.items = charge
        order.paid = 500
        order.save()
        return render(request, 'stripess/charge.html')


def newmethod(request):
    msg = ""
    sts = ""
    if request.method == 'POST':
        total = 20
        customer = stripe.Customer.create(
            email=request.POST["email"],
            name=request.POST['firstname'],
            source=request.POST['stripeToken']
        )
        charge = stripe.Charge.create(
            customer=customer,
            amount=total*100,
            currency='usd',
            description="Donation"
        )
        msg = "You have Donated Successfully"
        sts = "success"
    return render(request, 'stripess/newmethod.html', {'msg': msg, 'sts': sts})

