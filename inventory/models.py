from django.db import models
from laptop_shop.models import Product, Vendor, Branch
from laptop_shop.mixins import TimestampMixin

class GlobalInventory(TimestampMixin):
    product = models.ForeignKey(
      Product, on_delete=models.CASCADE, null=True, default=None)
    vendor = models.ForeignKey(
      Vendor, on_delete=models.SET_NULL, null=True, default=None)
    quantity = models.PositiveIntegerField(default=0)


class LocalInventory(TimestampMixin):
    branch = models.ForeignKey(
      Branch, on_delete=models.SET_NULL, null=True, default=None)
    quantity = models.PositiveIntegerField(default=0)
    globalInventory = models.ForeignKey(GlobalInventory, on_delete=models.SET_NULL, null=True, related_name='locals')

