from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    request.session['user_id'] = user.id
