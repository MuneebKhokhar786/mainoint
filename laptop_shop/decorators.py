from functools import wraps
from django.http import JsonResponse
from django.core.cache import cache

def ajax_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        user_id = cache.get('user_id')
        if user_id:
            return view_func(request, user_id=user_id, *args, **kwargs)
        return JsonResponse({ 'not_authenticated': True })
    return wrapper
