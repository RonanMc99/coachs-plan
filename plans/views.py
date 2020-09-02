from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Plan, Section

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

def section_details(request, plan_slug, section_number):
    section_qs = Section.objects \
        .filter(plan__slug=plan_slug) \
        .filter(section_number=section_number)
    if section_qs.exists():
        context = {
            'section': section_qs[0],
        }
        return render(request, "section_detail.html", context)
    return Http404