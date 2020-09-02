from django.shortcuts import render

from .models import Plan

def list_plans(request):
    queryset = Plan.objects.all()
    context = {
        'queryset': queryset
    }
    return render(request, "plans-list.html", context)
