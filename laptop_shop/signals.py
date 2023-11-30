from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.core.cache import cache

@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    cache.set('user_id', user.id, timeout=7200)
