from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from plans.models import Plan
from .models import CartItem, CompletedOrder, Order

import stripe
stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

@login_required
def add_to_cart(request, plan_slug):
    plan = get_object_or_404(Plan, slug=plan_slug)
    cart_item, created = CartItem.objects.get_or_create(plan=plan)
    order, created = Order.objects.get_or_create(
        user=request.user, purchased=False)
    order.items.add(cart_item)
    order.save()
    messages.info(request, "Added to Cart!")
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

@login_required
def remove_from_cart(request, plan_slug):
    plan = get_object_or_404(Plan, slug=plan_slug)
    cart_item = get_object_or_404(CartItem, plan=plan)
    order = get_object_or_404(Order, user=request.user)
    order.items.remove(cart_item)
    order.save()
    messages.info(request, "Removed from Cart!")
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

@login_required
def cart_view(request):
    order = get_object_or_404(Order, user=request.user)
    context = {
        'order': order
    }
    return render(request, "cart-summary.html", context)

@login_required
def checkout(request):
    order = get_object_or_404(Order, user=request.user)
    if request.method == "POST":

        # Get the stripe token
        token = request.POST.get('stripeToken')
        
        # `source` is obtained with Stripe.js; see https://stripe.com/docs/payments/accept-a-payment-charges#web-create-token
        charge = stripe.Charge.create(
            amount=int(order.get_order_total() * 100),
            currency="gbp",
            source=token,
            description=f"{request.user.username}s Order",
        )

        # Create an instance of CompletedOrder for this order
        completed_order = CompletedOrder()
        completed_order.order = order
        completed_order.payment_total = order.get_order_total()
        completed_order.stripe_ref = charge.id
        completed_order.save()

        # Add to the user's library of plans
        plans = [item.plan for item in order.items.all()]
        for plan in plans:
            request.user.usersplans.plans.add(plan)
        
        order.purchased = True
        order.save()
        messages.success(request, "Your order was placed successfully")
        return redirect("/account/profile/")
    
    context = {
        'order': order
    }

    return render(request, "checkout.html", context)
