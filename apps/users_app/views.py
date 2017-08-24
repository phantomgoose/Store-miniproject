# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.shortcuts import render, redirect, reverse, HttpResponse
import requests, json
from .google_auth import CLIENT_ID

class UsersIndex(View):
    def get(self, request):
        return render(request, 'users_app/users_index.html')

class UsersRedirect(View):
    def get(self, request):
        return redirect(reverse('users-index'))

class UsersLogin(View):
    def post(self, request):
        print 'got login post'
        id_token = request.POST['id_token']
        validation_url = 'https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=' + id_token
        server_response = {
            'logged_in': False,
            'redirect': reverse('users-index'),
        }
        try:
            google_response = json.loads(requests.get(validation_url).content)
            if google_response['aud'] == CLIENT_ID:
                request.session['user_id'] = google_response['sub']
                print 'login success'
                server_response['logged_in'] = True
                server_response['redirect'] = reverse('store-index')
        except Exception:
            print Exception, Exception.message
            print 'login failure'
        print 'returning json'
        return HttpResponse(json.dumps(server_response))

class UsersLogout(View):
    def get(self, request):
        request.session.flush()
        server_response = {
            'logged_out': True,
        }
        return HttpResponse(json.dumps(server_response))