from django.db import models
import json
from cloudinary.models import CloudinaryField
from .mixins import CloudinaryImageMixin, TimestampMixin
from accounts.models import CustomUser as User
from django.urls import reverse
from django.utils.text import slugify


class Collection(CloudinaryImageMixin, TimestampMixin):
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField()
    image = CloudinaryField('image', folder='main_point/collections/images/',
                            transformation={
                                'width': 600,
                                'height': 400,
                                'crop': 'fill',
                            })

    def __str__(self):
        return self.name


class Manufacturer(TimestampMixin):
    name = models.CharField(max_length=255)

class Product(TimestampMixin):
    name = models.TextField(db_index=True)
    description = models.TextField()
    details = models.TextField(null=True, blank=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    price_compare_to = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    slug = models.SlugField(null=True, unique=True, db_index=True)

    collection = models.ForeignKey(
        Collection, on_delete=models.SET_NULL, null=True, blank=True, db_index=True)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.SET_NULL, null=True, blank=True, db_index=True)
    
    @property
    def discount_percentage(self):
        if self.price_compare_to > self.price:
            discount = ((self.price_compare_to - self.price) / self.price_compare_to) * 100
            return int(round(discount))
        return None

    def __str__(self):
        fields = {
            'name': self.name,
            'price': str(self.price),
            'slug': self.slug,
        }
        return json.dumps(fields)

    def __repr__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse("show", kwargs={"product_slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            if len(self.name) < 41:
                slug_name = self.name
            else:
                slug_name = self.name[:40]

            self.slug = slugify(slug_name)
        return super().save(*args, **kwargs)

class ProductImage(CloudinaryImageMixin, TimestampMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image', folder='main_point/products/images/',
                            transformation={
                                'width': 600,
                                'height': 600,
                                'crop': 'fill',
                            })

    def __str__(self):
        return self.product.name

class ProductVideo(TimestampMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='videos')
    video = CloudinaryField('video', folder='main_point/products/videos/', resource_type='video',blank=True, null=True)

    def __str__(self):
        return self.product.name

class Order(TimestampMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"Order #{self.pk} - {self.user.username}"

class OrderItem(TimestampMixin):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Order #{self.order.pk} - {self.product.name} - Quantity: {self.quantity}"

class Vendor(TimestampMixin):
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField()

    def __str__(self):
        return self.name

class Branch(TimestampMixin):
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField()

    def __str__(self):
        return self.name or self.address

