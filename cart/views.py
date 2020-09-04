from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from plans.models import Plan
from .models import CartItem, CompletedOrder, Order

def add_to_cart(request, plan_slug):
    plan = get_object_or_404(Plan, slug=plan_slug)
    cart_item, created = CartItem.objects.get_or_create(plan=plan)
    order, created = Order.objects.get_or_create(
        user=request.user, purchased=False)
    order.items.add(cart_item)
    order.save()
    messages.info(request, "Added to Cart!")
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def cart_view(request):
    order = get_object_or_404(Order, user=request.user)
    context = {
        'order': order
    }
    return render(request, "cart-summary.html", context)
