# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from users.models import User

# Create your views here.
# The default home page view.
def home_page(request):

    user = request.user
    
    return render(request, "home.html", {"user": user})