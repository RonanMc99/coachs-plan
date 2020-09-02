from django.contrib import admin

from .models import Coach, Plan, Section, Activity, Example

admin.site.register(Coach)
admin.site.register(Plan)
admin.site.register(Section)
admin.site.register(Activity)
admin.site.register(Example)