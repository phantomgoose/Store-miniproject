from django.shortcuts import redirect, reverse, HttpResponse
import json

def login_required(func):
    def wrapper(request, *args, **kwargs):
        if 'user_id' not in request.session.keys() or len(request.session['user_id']) < 1:
            return HttpResponse('You need to be logged in to do that.')
        return func(request, *args, **kwargs)
    return wrapper

def admin_required(func):
    def wrapper(request, *args, **kwargs):
        if 'admin' not in request.session.keys() or request.session['admin'] is not True or 'user_id' not in request.session.keys() or len(request.session['user_id']) < 1:
            return HttpResponse('You need to be an admin to do that.')
        return func(request, *args, **kwargs)
    return wrapper