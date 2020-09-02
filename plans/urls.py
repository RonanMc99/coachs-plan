from django.urls import path
from .views import list_plans, plan_details

app_name = 'plans'

urlpatterns = [
    path('', list_plans, name='plans-list'),
    path('<slug>/', plan_details, name='plan-details'), 
]