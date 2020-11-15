from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Plan, Section, Activity
from cart.models import Order, CartItem

IN_CART = "in_cart"
NOT_IN_CART = "not_in_cart"
IS_OWNED = "owned"


def check_ownership(request, plan):

    if plan in request.user.usersplans.plans_list():
        return IS_OWNED
    order_qs = Order.objects.filter(user=request.user)
    if order_qs.exists():
        order = order_qs[0]
        order_item_qs = CartItem.objects.filter(plan=plan)
        if order_item_qs.exists():
            order_item = order_item_qs[0]
            if order_item in order.items.all():
                return IN_CART
    return NOT_IN_CART


def list_plans(request):
    queryset = Plan.objects.all()
    context = {"queryset": queryset}
    return render(request, "plan-list.html", context)


@login_required
def plan_details(request, slug):
    plan = get_object_or_404(Plan, slug=slug)
    plan_ownership = check_ownership(request, plan)
    context = {"plan": plan, "plan_ownership": plan_ownership}
    return render(request, "plan-detail.html", context)


@login_required
def section_details(request, plan_slug, section_number):
    section_qs = Section.objects.filter(plan__slug=plan_slug).filter(
        section_number=section_number
    )
    section = section_qs[0]
    plan_ownership = check_ownership(request, section.plan)
    if section_qs.exists():
        context = {"section": section, "plan_ownership": plan_ownership}
        return render(request, "section_detail.html", context)
    return Http404


@login_required
def activity_details(request, plan_slug, section_number, activity_number):
    activity_qs = (
        Activity.objects.filter(section__plan__slug=plan_slug)
        .filter(section__section_number=section_number)
        .filter(activity_number=activity_number)
    )
    activity = activity_qs[0]
    plan_ownership = check_ownership(request, activity.section.plan)
    if activity_qs.exists():
        context = {"activity": activity, "plan_ownership": plan_ownership}
        return render(request, "activity-detail.html", context)
    return Http404
