from django.urls import path

app_name = 'plans'

urlpatterns = [
    path('', list-plans, name='plans-list')
]