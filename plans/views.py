from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Plan, Section, Activity
from cart.models import Order, CartItem


def list_plans(request):
    queryset = Plan.objects.all()
    context = {"queryset": queryset}
    return render(request, "plan-list.html", context)


@login_required
def plan_details(request, slug):
    plan = get_object_or_404(Plan, slug=slug)
    order_qs = Order.objects.filter(user=request.user)
    plan_in_cart = False
    if order_qs.exists():
        order = order_qs[0]
        order_item_qs = CartItem.objects.filter(plan=plan)
        if order_item_qs.exists():
            order_item = order_item_qs[0]
            if order_item in order.items.all():
                plan_in_cart = True
    context = {"plan": plan, "in_cart_item": plan_in_cart}
    return render(request, "plan-detail.html", context)


@login_required
def section_details(request, plan_slug, section_number):
    section_qs = Section.objects.filter(plan__slug=plan_slug).filter(
        section_number=section_number
    )
    if section_qs.exists():
        context = {
            "section": section_qs[0],
        }
        return render(request, "section_detail.html", context)
    return Http404


@login_required
def activity_details(request, plan_slug, section_number, activity_number):
    activity_qs = (
        Activity.objects.filter(section__plan__slug=plan_slug)
        .filter(section__section_number=section_number)
        .filter(activity_number=activity_number)
    )
    if activity_qs.exists():
        context = {
            "activity": activity_qs[0],
        }
        return render(request, "activity_detail.html", context)
    return Http404