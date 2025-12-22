from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.db.models.signals import post_delete
from .models import ProductImage

import cloudinary.uploader

@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    request.session['user_id'] = user.id

@receiver(post_delete, sender=ProductImage)
def delete_cloudinary_image(sender, instance, **kwargs):
    breakpoint()
    if instance.image:
        cloudinary.uploader.destroy(public_id=instance.image.public_id)