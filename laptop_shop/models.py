from django.db import models
from cloudinary.models import CloudinaryField
from .mixins import CloudinaryImageMixin
from django.urls import reverse
from django.utils.text import slugify


class Collection(CloudinaryImageMixin, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image', folder='main_point/collections/images/',
                            transformation={
                                'width': 600,
                                'height': 400,
                                'crop': 'fill',
                            })

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(null=True, unique=True)

    collection = models.ForeignKey(
        Collection, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("index", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class ProductImage(CloudinaryImageMixin, models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image', folder='main_point/products/images/',
                            transformation={
                                'width': 600,
                                'height': 600,
                                'crop': 'fill',
                            })

    def __str__(self):
        return self.product.name
