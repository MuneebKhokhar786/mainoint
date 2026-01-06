from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from .models import ProductImage, Collection, ProductVideo

import cloudinary.uploader

@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    request.session['user_id'] = user.id

@receiver(pre_delete, sender=Collection)
@receiver(pre_delete, sender=ProductImage)
def delete_cloudinary_image(sender, instance, **kwargs):
    print("PRE_DELETE:", sender.__name__)
    print("PUBLIC ID:", getattr(instance.image, 'public_id', None))
    if instance.image:
        result=cloudinary.uploader.destroy(public_id=instance.image.public_id, resource_type="image")
        print("Cloudinary Image result: ", result)

@receiver(pre_delete, sender=ProductVideo)
def delete_cloudinary_video(sender, instance, **kwargs):
    print("PRE_DELETE:", sender.__name__)
    print("PUBLIC ID:", getattr(instance.video, 'public_id', None))
    if instance.video:
        try:
            result=cloudinary.uploader.destroy(public_id=instance.video.public_id, resource_type="video")
            print("Cloudinary Video Result: ", result)
        except:
            print("cant delete video")