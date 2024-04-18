from django.db import models
import cloudinary.uploader

class CloudinaryImageMixin(models.Model):
    class Meta:
        abstract = True

    def delete_cloudinary_image(self):
        if self.image:
            cloudinary.uploader.destroy(self.image.public_id)

    def delete_old_cloudinary_image(self):
        try:
            current_instance = self.__class__.objects.get(pk=self.pk)
            if current_instance.image != self.image:
                current_instance.delete_cloudinary_image()
        except self.__class__.DoesNotExist:
            pass

    def delete(self, *args, **kwargs):
        self.delete_cloudinary_image()
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.delete_old_cloudinary_image()
        super().save(*args, **kwargs)

class TimestampMixin(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
