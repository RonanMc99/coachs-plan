from django.shortcuts import render, get_object_or_404

from .models import Plan

def list_plans(request):
    queryset = Plan.objects.all()
    context = {
        'queryset': queryset
    }
    return render(request, "plan-list.html", context)

def plan_details(request, slug):
    plan = get_object_or_404(Plan, slug=slug)
    context = {
        'plan': plan
    }
    return render(request, "plan-detail.html", context)