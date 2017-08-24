from django.shortcuts import redirect, reverse

def login_required(func):
    def wrapper(request, *args, **kwargs):
        if 'user_id' not in request.session.keys() or len(request.session['user_id']) < 1:
            return redirect(reverse('users-index'))
        return func(request, *args, **kwargs)
    return wrapper