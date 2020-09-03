from django.conf import settings
from django.db import models
from plans.models import Plan

import uuid

class Order(models.Model):
    ''' The user's order '''
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE)
    order_ref = models.UUIDField(default=uuid.uuid4, editable=False)
    items = models.ManyToManyField('CartItem')
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email


class CartItem(models.Model):
    ''' An item in the cart '''
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    def __str__(self):
        return self.plan.title


class CompletedOrder(models.Model):
    ''' A completed order '''
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_total = models.FloatField()
    stripe_ref = models.CharField(max_length=150)

    def __str__(self):
        return self.stripe_ref