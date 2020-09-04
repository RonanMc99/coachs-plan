from django.urls import path
from .views import add_to_cart, cart_view, checkout

app_name = 'cart'

urlpatterns = [
    path('add_to_cart/<plan_slug>/', add_to_cart, name='add_to_cart'),
    path('cart_summary/', cart_view, name='cart_summary'),
    path('checkout/', checkout, name='checkout'),
]