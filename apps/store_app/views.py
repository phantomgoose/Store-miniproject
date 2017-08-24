# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from ..helper_functions import login_required

class StoreIndex(View):
    def get(self, request):
        return render(request, 'store_app/store_index.html')