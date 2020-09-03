from django.contrib import admin
from .models import CartItem, CompletedOrder, Order

admin.site.register(CartItem)
admin.site.register(CompletedOrder)
admin.site.register(Order)
