from django import template
from cart.models import Order

register = template.Library()


@register.filter
def cart_item_counter(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, purchased=False)
        if qs.exists():
            return qs[0].items.count()
    return 0
