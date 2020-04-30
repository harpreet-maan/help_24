# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render,redirect

# Create your views here.
def register(request):
    if request.method=='POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        un = request.POST['username']
        em = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if pass1==pass2:
            if User.objects.filter(username=un).exists():
                print('username taken !')
            elif User.objects.filter(email=em).exists():
                print('email taken !')
            else:
                user = User.objects.create_user(username=un, email=em, password=pass1, first_name=fn, last_name=ln)
                user.save()
        else:
            return redirect('/register')
    else:
        return render(request,'register.html')