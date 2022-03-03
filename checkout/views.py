from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse,('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KZB4PGGWCtwolp3EfX9qUGKaDgw1du1gNqJXYIqrdAHiI13IksnIu6Fr38h80kcDKsHOLMZyLIwdR7WUoOj70Qp00th0fWx6K',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
