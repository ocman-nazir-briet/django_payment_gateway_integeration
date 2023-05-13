from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.views.generic.base import TemplateView
from .models import *
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

class home(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["key"] = settings.STRIPE_PUBLISHABLE_KEY 
        context["paypal_key"] = settings.PAYPAL_PUBLISHABLE_KEY 
        return context

# Stripe Payment Gateway Integeration 
def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount = 50,
            currency='USD',
            description = 'test payment',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')
    return HttpResponse('Payment Unsuccessful')

# Paypal Payment Gateway Integeration
def charge_paypal(request):
    pass