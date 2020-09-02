from django.urls import path
from .views import list_plans

app_name = 'plans'

urlpatterns = [
    path('', list_plans, name='plans-list')
]