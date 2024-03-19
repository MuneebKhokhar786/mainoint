from functools import wraps
from django.http import JsonResponse

def ajax_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        user_id = request.session.get('user_id', None)
        if user_id:
            return view_func(request, user_id=user_id, *args, **kwargs)
        return JsonResponse({ 'not_authenticated': True })
    return wrapper
