from django.contrib import admin

from .models import Coach, Plan, Section, Activity, Example, UsersPlans

admin.site.register(Coach)
admin.site.register(Plan)
admin.site.register(Section)
admin.site.register(Activity)
admin.site.register(Example)
admin.site.register(UsersPlans)